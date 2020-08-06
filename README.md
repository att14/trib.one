# trib.one

My personal website.

## Style

The style of this site is inspired by Edward Tufte's books and handouts. The most defining feature of this design is the large margin on every page and extensive use of side-notes. This layout means that the central column of text is uncluttered since further descriptions and citations are housed in the margin.

Tufte also coined the terms _chartjunk_ and _data-ink ratio_ to argue against using excessive decoration in visual displays of quantitative information. This site tries to adhere to this philosophy by not cluttering pages with unnecessary information.

## Pandoc

The pages of this site are written as Markdown and converted to HTML via [_Pandoc_](https://pandoc.org/index.html). Tufte's style is achieved by using [_Tufte Pandoc CSS_](https://jez.io/tufte-pandoc-css/).

### Watching Markdown with `glow` and `entr`

[`glow`](https://github.com/charmbracelet/glow) allows for markdown files to be rendered in your terminal. [`entr`](https://github.com/clibs/entr) is a utility for running arbitrary commands when files changed. Together you can use them to watch the render while you are editing them without an external application like [Marked](https://github.com/markedjs/marked).

```sh
function watchmd() {
    sh -c "ls $1" | entr -r glow "$1"
}
```
