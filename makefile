.PHONY: build clean apply package

gen = generator
out = output
temp = $(gen)/template
freq = $(gen)/freq
table = $(gen)/table

word_freq = $(freq)/word.txt
phrase_freq = $(freq)/phrase.txt

mapping = $(table)/yi_components_mapping.txt
spelling = $(table)/yi_spelling.txt
fullcode = $(table)/yi_fullcode_table.txt
word = $(table)/yi_table.txt
phrase = $(table)/yi_phrase_table.txt

build: $(word) $(phrase) $(spelling)
	mkdir -p $(out)
	# 拷贝生成模板
	rsync -a $(temp)/ $(out)/
	# 拆分提示
	cat $(spelling) > $(out)/opencc/division.txt
	# 单字码表
	$(gen)/dict-gen.py -t $(word) >> $(out)/ymdz.dict.yaml
	# 空格词码表
	$(gen)/dict-gen.py -t $(phrase) >> $(out)/ym.phrases.dict.yaml

apply: $(out)
	# 输出到 ibus-rime 配置
	rsync -a $(out)/ ~/.config/ibus/rime/

package: $(out)
	# 打包发布
	cd $(out) && atool -a /tmp/rime-yima.zip ./*

clean:
	# 清理生成
	-rm $(fullcode) $(word) $(phrase) 2> /dev/null
	-rm -r $(out) 2> /dev/null

$(out): build

$(word): $(fullcode) $(word_freq)
	# 生成单字码表
	$(gen)/word-gen.py -f $(word_freq) -c $(fullcode) > $(word) 2> /dev/null

$(phrase): $(word) $(fullcode) $(phrase_freq)
	# 生成分号词码表
	$(gen)/phrase-gen.py -f $(phrase_freq) -c $(fullcode) -t $(word) > $(phrase) 2> /dev/null

$(fullcode): $(mapping) $(spelling)
	# 生成单字全码码表
	$(gen)/fullcode-gen.py -m $(mapping) -s $(spelling) > $(fullcode) 2> /dev/null
