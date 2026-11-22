# Website source — HowsenLiu Fangrun · 柳皓升方润黑体

Static site published at <https://howsenliufangrun.pages.dev>. Plain HTML / CSS / JS, no build step.

## Structure

| Path | Contents |
|---|---|
| `index.html` | Single-page markup; bilingual UI, seven showcase panels |
| `css/styles.css` | Layout, theme and component styles |
| `js/main.js` | Bilingual dictionary, panel rotation, reveal and entrance animations |
| `assets/` | Favicon and logo mark |
| `fonts/webfonts/` | Site subset WOFF2 + demo WOFF2 used by the live page; `page-charset.txt` lists the covered code points |
| `OFL-LICENSE.txt` | Full SIL OFL 1.1 license text for the bundled web fonts |

> The WOFF2 files here are the page-specific subset used by this site. The wider GB2312
> subset and full-charset WOFF2 live under `fonts/webfonts/` in the repository root and in
> the Release packages.

## Run locally

Open `index.html` directly in a browser, or serve the folder:

```bash
npx serve .
```

## License

The bundled web fonts are released under the **SIL Open Font License 1.1** — see
`OFL-LICENSE.txt`. Free for personal and commercial use; modification and derivatives are
allowed, but derivatives must remain under OFL 1.1 and keep the copyright notice and full
license text. The font files may not be sold standalone.
