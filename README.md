# mdsummary

A simple python3 script who create a simple summary to markdown file

## Pre-requisite

- python3
- Markdown format:
  - The file must have a title on the first line
  - The second line must be blank/empty
  - The third line must be a little description or h2
  - After the little description, if there is one, use a h2.
If you don't use a h2, you won't have a summary

## Usage

Add a summary in a new file :

```bash
./mdsummary.py test/test1.md test1_with_summary.md
```

Add a summary in the same file :

```bash
cp test/test1.md .
./mdsummary.py test1.md
```

## Usefull ?

Not very much because github.com have a fonctionnality of summary in their application.
Can be usefull if you want that your file can be read outside github

Enjoy and have fun!
