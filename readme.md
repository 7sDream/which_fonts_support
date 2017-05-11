# Which fonts support

[English Readme](#introduction)

## 介绍

一个查看系统上哪些字体支持给定的字符的小脚本。

是因为最近在做 LaTeX 的时候，经常需要处理特殊字符，用个备用字体显示什么的。

于是就写了个这个小东西帮我找出可用的字体。

应该没有其他人有这个需求了吧。

### 使用方法：

```bash
./which_fonts_support.sh <单个字符>
```

### 依赖：

* fontconfig
* python3
* bash

## Introduction

A small scirpt to find which fonts support specified character.

Recently, I'm working on a LaTeX project, and need to deal with special characters(use another fallback font to show it) frequently.

So I write this to help me find avaliable fallback font in my system.

(There should be no other people have this demand, I think...

### Usage

```bash
./which_fonts_support.sh <the-char>
```

### Dependencies

* fontconfig
* python3
* bash

## 截图 / Screenshot

正常使用/normal usage：

![][screen-shot-normal]

你也可以通过 `sort` 排序然后 `uniq` 去重，将不同字型/自重的相同字体合并：

You can use `sort` command and `uniq` command to sort and union different weight/style of same font：

![][screen-shot-sort-uniq]

## LICENSE

MIT.

[screen-shot-normal]: http://rikka-10066868.image.myqcloud.com/5da3375e-953c-4f63-9afb-ab42177b0fae.png
[screen-shot-sort-uniq]: http://rikka-10066868.image.myqcloud.com/d1738c23-97a8-4167-8daf-7b48a7baecbd.png
