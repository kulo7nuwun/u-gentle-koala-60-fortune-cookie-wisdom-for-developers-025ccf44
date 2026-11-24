# Fortune Cookie Wisdom for Developers

[![make.fun](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/c/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

Entry for the make.fun competition
[Fortune Cookie Wisdom for Developers](https://make.fun/c/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44):
write one original line of fortune-cookie wisdom aimed at a software
developer, at most 120 characters.

## The line

> The legacy code you curse was once a clever fix on a tired Friday.

## How it works

`main.py` writes that single line to `entry.txt` in the output directory
(`/output` by default, or `$MAKEFUN_OUTPUT_DIR` when set). No network,
no dependencies, no secrets — just the standard library.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
