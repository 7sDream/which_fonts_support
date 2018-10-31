# Which fonts support

[English Readme](#introduction)

## 介绍

一个查看系统上哪些字体支持给定的字符的小脚本。

是因为最近在做 LaTeX 的时候，经常需要处理特殊字符，用个备用字体显示什么的。

于是就写了个这个小东西帮我找出可用的字体。

应该没有其他人有这个需求了吧。

### 使用方法：

```bash
./which_fonts_support.py <单个字符>
```

### 依赖：

* fontconfig
* python3

## Introduction

A small scirpt to find which fonts support specified character.

Recently, I'm working on a LaTeX project, and need to deal with special characters(use another fallback font to show it) frequently.

So I write this to help me find avaliable fallback font in my system.

(There should be no other people have this demand, I think...

### Usage

```bash
./which_fonts_support.py <the-char>
```

### Dependencies

* fontconfig
* python3

## 截图 / Screenshot

![][screen-shot-normal]

## LICENSE

MIT.

[screen-shot-normal]: https://i.loli.net/2018/10/31/5bd9c90ab5333.jpg
