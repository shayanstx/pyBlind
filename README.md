# pyBlind - Blind Analyzer
Analyze your Site for Blind-Sql Injection Vulnerability.

## About
If you are a web security expert or have a personal website, you should make sure that there are no security vulnerabilities on the website.
One of these vulnerabilities is the `Blind-Sql Injection` vulnerability that is seen in many sites and can be used to obtain sensitive information from the target system.
`pyBlind` helps you to go through this process very easily and quickly and reach vulnerability.

## Requirements
You need Python 3.0 to run This Tool.

## Usage
```
$ Python3 pyblind.py -u <URL>
```

## Options
Usage : pyblind [options]
```
-h          show help Menu
-u          set a <URL> for analyze
-V          Get database Version
-T          Get db Tables
-C          Get db Columns
--dbs       Database Methode
--like      Like Methode
--list      List Methode
```

## Example
```
$ python3 pyblind.py -u https://example.com/index.php?id=1 -T --dbs
```

## Developer
    * shayanstx
    instagram.com/shayanstx
    shayanstx@gmail.com