# pre-commit-xmllint

This is a [pre-commit](https://pre-commit.com) hook that supports formatting XML
files through two possible methods:

- xmllint (id: `xmllint-format`)
- python+lxml (id: `lxml-format`)

## Example usage:

```yaml
  - repo: https://github.com/GlodoUK/pre-commit-xmllint
    rev: commithash
    hooks:
      - id: lxml-format
```
