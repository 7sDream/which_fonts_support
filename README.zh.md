# Which fonts support

## 介绍

一个查看系统上哪些字体支持给定的字符的小脚本。

是因为最近在做 LaTeX 的时候，经常需要处理特殊字符，用个备用字体显示什么的。

于是就写了个这个小东西帮我找出可用的字体。

应该没有其他人有这个需求了吧。

## 安装

```bash
pip3 install which-fonts-support
```

## 使用

```bash
which_fonts_support <单个字符>

# 或者

python3 -m which_fonts_support.cli <单个字符>
```

如果希望检测非 BMP 平面字符，请在上述 `<单个字符>` 处使用 `U+XXXX` 或者 `U+XXXXXX` 形式。

添加 `-v` 参数可以显示字体的所有样式。

添加 `-p` 参数可以在浏览器里预览这些字体的显示效果。

使用 `-f path` 参数可以自定义 `fc-list` 可执行文件的安装位置。

见后文截图。

## 依赖：

* python >= 3.5
* 系统已安装 `fontconfig`

## 截图

### 普通使用

![][screen-shot-normal]

### 显示所有样式

此[截图][screen-shot-verbose]较长，请点击查看。

### 预览

![][screen-shot-preview]

前端苦手，这已经是我能做到最好的样子了，如果有老哥愿意帮忙美化一下，感激不尽。

## TODO

- [x] 生成 HTML 用于预览字体
- [x] 可以作为模块使用
- [x] 使用内置 HTTP 服务器提供网页预览支持，不再使用临时文件
- [ ] 文档
- [ ] 在 PyPI 上增加描述
- [ ] 写一篇关于 `fc-list` 命令的小文章

## LICENSE

MIT.

[screen-shot-normal]: https://rikka.7sdre.am/files/a3ba7846-4d13-4719-aa31-08121d549099.png
[screen-shot-verbose]: https://rikka.7sdre.am/files/3b46d5ed-54f0-414f-b19b-26c5468d2225.png
[screen-shot-preview]: https://rikka.7sdre.am/files/5b180f2f-6255-4330-958c-472a1520e3ad.png
