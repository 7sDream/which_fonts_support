# Which fonts support

[中文版本][chinese-readme]

## Introduction

A small script to find which fonts support specified character.

Recently, I'm working on a LaTeX project, and need to deal with special characters(use another fallback font to show it) frequently.

So I write this to help me find available fallback font in my system.

(There should be no other people have this demand, I think...

## Install

```bash
pip3 install which-fonts-support
```

### Usage

```bash
which_fonts_support <the-char>

# Or

python3 -m which_fonts_support.cli <the-char>
```

Use `U+XXXX` or `U+XXXXXX` format for non BMP character.

Add `-v` to show all style of those fonts.

Add `-p` to show display preview of those font in browser.

Use `-f <path>` to use your `fc-list` installed in a custom path.

## Environment requirements

* python >= 3.5
* `fontconfig` installed in your system

## Screenshot

### Normal usage

![][screen-shot-normal]

### Show all styles

This [screenshot][screen-shot-verbose] is a little big, please click to see it.

### Preview

![][screen-shot-preview]

I'm poor in design and HTML works, this preview is designed and implemented by [@MashiroWang][MashiroWang-github], thanks!

## TODO

- [x] generate HTML page for preview fonts
- [x] Make it can be used as a module
- [x] Use an internal http server to support preview, instead of temp file
- [ ] Documents
- [ ] Add words on PyPI page
- [ ] Article about `fc-list` command

## LICENSE

MIT.

[chinese-readme]: https://github.com/7sDream/which_fonts_support/blob/master/README.zh.md
[screen-shot-normal]: https://rikka.7sdre.am/files/a3ba7846-4d13-4719-aa31-08121d549099.png
[screen-shot-verbose]: https://rikka.7sdre.am/files/3b46d5ed-54f0-414f-b19b-26c5468d2225.png
[screen-shot-preview]: https://rikka.7sdre.am/files/2b7d5421-3e6b-4a65-a36c-73b8436d962d.png
[MashiroWang-github]: https://github.com/MashiroWang
