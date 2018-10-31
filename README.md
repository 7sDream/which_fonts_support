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

### Dependencies

* fontconfig
* python >= 3.5
* wcwidth

## 截图 / Screenshot

![][screen-shot-normal]

## LICENSE

MIT.

[screen-shot-normal]: https://i.loli.net/2018/11/01/5bda081e2b840.jpg
