# syntax=docker/dockerfile:1
# HowsenLiu Fangrun — free OFL 1.1 font bundle published to GitHub Container Registry.
# Context is assembled by .github/workflows/publish-package.yml from the latest Release assets.
FROM scratch

LABEL org.opencontainers.image.title="HowsenLiu Fangrun (柳皓升方润黑体)" \
      org.opencontainers.image.description="Free OFL 1.1 font bundles: desktop TTF / TTC / variable TTF and web WOFF2" \
      org.opencontainers.image.licenses="OFL-1.1" \
      org.opencontainers.image.source="https://github.com/HowsenLiu/HowsenLiuFangrun"

COPY fonts/ /fonts/
