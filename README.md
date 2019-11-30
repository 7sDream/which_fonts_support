# Which fonts support

[English Readme](#introduction)

## 介绍

一个查看系统上哪些字体支持给定的字符的小脚本。

是因为最近在做 LaTeX 的时候，经常需要处理特殊字符，用个备用字体显示什么的。

于是就写了个这个小东西帮我找出可用的字体。

应该没有其他人有这个需求了吧。

### 使用方法：

```bash
pip3 install which-fonts-support
which_fonts_support <单个字符>
```

如果希望检测非 BMP 平面字符，请使用 `U+XXXX` 或者 `U+XXXXXX` 格式。

添加 `-v` 参数可以显示字体的所有样式。

添加 `-p` 参数可以在浏览器里预览这些字体的显示效果。

使用 `-f path` 参数可以自定义 `fc-list` 可执行文件的安装位置。

见后文截图。

### 依赖：

* 已安装 `fontconfig`
* python >= 3.5
* wcwidth >= 0.1.7

## Introduction

A small script to find which fonts support specified character.

Recently, I'm working on a LaTeX project, and need to deal with special characters(use another fallback font to show it) frequently.

So I write this to help me find available fallback font in my system.

(There should be no other people have this demand, I think...

### Usage

```bash
pip3 install which-fonts-support
which_fonts_support <the-char>
```

Use `U+XXXX` or `U+XXXXXX` format for non BMP character.

Add `-v` to show all style of those fonts.

Add `-p` to show display preview of those font in browser.

Use `-f <path>` to use your `fc-list` installed in a custom path.

### Dependencies

* `fontconfig` installed in your system
* python >= 3.5
* wcwidth

## 截图 / Screenshot

### 普通使用 / Normal usage

![][screen-shot-normal]

### 显示所有样式 / Show all styles

此[截图][screen-shot-verbose]较长，请点击查看。

This [screenshot][screen-shot-verbose] is a little big, please click to see it.

### 预览 / Preview

![][screen-shot-preview]

前端苦手，这已经是我能做到最好的样子了，如果有老哥愿意帮忙美化一下，感激不尽。

I'm poor in design and HTML works, this is already my most successful try. If anyone willing to help me turn it to a elegant page, I would be grateful.  

## TODO

- [x] generate HTML page for preview fonts
- [x] Make this a module
- [x] Use an internal http server to preview, not temp file
- [ ] Documents
- [ ] Add words on pypi page
- [ ] Article about how to read the charset section of `fc-list` command

## LICENSE

MIT.

[screen-shot-normal]: https://rikka.7sdre.am/files/a3ba7846-4d13-4719-aa31-08121d549099.png
[screen-shot-verbose]: https://rikka.7sdre.am/files/3b46d5ed-54f0-414f-b19b-26c5468d2225.png
[screen-shot-preview]: https://rikka.7sdre.am/files/5b180f2f-6255-4330-958c-472a1520e3ad.png
