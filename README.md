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

添加 `-v` 参数可以显示字体的所有样式。

添加 `-p` 参数可以在浏览器里预览这些字体的显示效果。

见后文截图。

### 依赖：

* fontconfig
* python >= 3.5
* wcwidth

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

Add `-p` to show display preview of those font in browser.

### Dependencies

* fontconfig
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
- [ ] Documents
- [ ] Add words on pypi page
- [ ] Article about how to read the charset section of `fc-list` command

## LICENSE

MIT.

[screen-shot-normal]: https://i.loli.net/2018/11/01/5bdb06aa01fb8.jpg
[screen-shot-verbose]: https://i.loli.net/2018/11/01/5bdb06ab906fc.jpg
[screen-shot-preview]: https://i.loli.net/2018/11/01/5bdb06aab5f1e.jpg
