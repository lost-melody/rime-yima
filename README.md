# 逸码

> 逸码是一个纯形码顶功方案, 由 *小泥巴* 于2018年设计

## 逸码文档

- 拆分码表源仓库: [lakent/yi][1]
- 逸码教程、文档及其他资料等参见QQ群: 790835977

## 本方案配置说明

- 单字方案, 二码开顶, 通过 `Ctrl+Shift+C` 切换拆分提示
- 按 `i` 进入拼音反查, 默认启用小鹤双拼
    - 可在 `ymdz.custom.yaml` 中修改 `rev_pinyin/prism` 以切换为全拼
- 按 `i` 进入四角号码反查, 以第一排字母键 `qwertyuiop` 代替数字键
- 竞争候选: 为所有唯一候选增加竞争候选, 于是即使唯一也不自动上屏
    - 在 `ymdz.main.dict.yaml` 和 `ym.phrases.main.dict.yaml` 中注释掉 `comp` 词库即可禁用此功能
- 在单字基础上增加空格出词
    - 单字上屏需要顶字或者连敲两下空格
    - 反查候选使用数字键选字
    - 二码后接空格出词
        - 二字词: 首字前二码+空格+次字全码
        - 多字词: 首字和次字的首码+空格+末字全码

## 自定义构建

如果只求正常使用, 直接将 `output` 且录下的配置文件复制到 *rime* 配置中即可

有词库自定义需要的, 可以替换 `generator/freq/phrase.txt` 文件, 再通过 *make* 工具完成构建:

```sh
# 开始构建, 并将生成配置输出到 `output`
make build
# 构建并将配置拷贝到 `.config/ibus/rime`, 即 *ibus-rime* 配置
make apply
# 构建并打包为发布文件 `rime-yima.zip`
make package
```

> 构建依赖
> - `make`
> - `rsync` (可用 `cp` 命令替代)
> - `atool` (仅打包发布使用, 可用任何其他压缩工具替代)
> - `python` (要求版本 *3.10+*)

## 数据来源声明

- 字频及词频数据: 逸码群单单字频词频表
- 方案拆分和字根映射码表: [lakent/yi][1]
- 四角号码反查码表: [zongxinbo/rime-zong][2]
- 袖珍简化字拼音码表: [rime/rime-pinyin-simp][3]
- 小鹤双拼配置: [rime/rime-double-pinyin][4]
- 方案细项配置: 自 *单单* 的逸码 *rime* 方案配置修改而来

[1]: https://jihulab.com/lakent/yi "极狐GitLab"
[2]: https://github.com/zongxinbo/rime-zong "Github"
[3]: https://github.com/rime/rime-pinyin-simp "Github"
[4]: https://github.com/rime/rime-double-pinyin "Github"

