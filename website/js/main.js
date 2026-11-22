/* ============================================================
   HowsenLiuFangrun · 交互脚本
   双语切换 / 首屏多语言大字轮播 / 语言舞台 / 字重滑块 / 字符墙 / 入场动效
   ============================================================ */

(function () {
  "use strict";

  /* ---------------------------------------------------------- 双语字典 */
  const I18N = {
    zh: {
      "nav.specimen": "样张",
      "nav.design": "设计",
      "nav.download": "下载",
      "nav.license": "授权",
      "brand.cn": "柳皓升®方润黑体",
      "meta.title": "柳皓升®方润黑体 · HowsenLiuFangrun",
      "hero.eyebrow": "HowsenLiu Fangrun · Typeface 2.000",
      "manifesto.line": "方折骨架，圆润收口。",
      "manifesto.sub": "一款为屏幕与印刷打磨的无衬线字体，字重连续可调，结构方折，细节柔和；同一副骨架，横跨多种文字。",
      "stage.title": "多语言展示",
      "stage.sub": "简体中文 · 繁體中文 · English · 日本語 · 한국어 · 欧洲语言 · 符号，切换查看同一副骨架。",
      "weight.title": "字重变化",
      "weight.sub": "同一副骨架，从细到粗只加厚笔画，圆角半径与结构比例保持不变。",
      "ax.wght": "厚度",
      "ax.wdth": "宽窄",
      "ax.opsz": "光学",
      "detail.title": "设计语言",
      "detail.macro": "圆角收口 · 同一半径",
      "sheet.radius": "R · 圆角半径全字统一",
      "sheet.angle": "骨架转角 90° · 圆角化",
      "sheet.frame": "字身框 1000 × 1000",
      "glyph.title": "字符覆盖",
      "glyph.sub": "常用汉字、谚文、欧洲字母与符号、假名、数字，同一视觉体系。",
      "f1.t": "统一圆角",
      "f1.d": "全部笔画转角与端点采用同一圆角半径，整套字风格一致、温和克制。",
      "f2.t": "大字符覆盖",
      "f2.d": "44,731 字形 / 44,828 码位，覆盖 GBK 全集、GB18030 一/二级、Big5、谚文音节与 Jamo、假名注音、希腊西里尔、变音字母与常用符号。",
      "f3.t": "多字重配套",
      "f3.d": "可变字重 100–700 连续可调，另附 Light / Regular / Medium / Bold 四款静态字重。",
      "dl.title": "下载字体",
      "dl.sub": "小体积子集可在本页直接下载；完整大包与历史发布见 GitHub Release。",
      "dl.variable.name": "可变完整包",
      "dl.variable.note": "可变字体全量包，桌面安装与设计软件使用。",
      "dl.static.name": "静态字重包",
      "dl.static.note": "Light / Regular / Medium / Bold 四款静态 TTF。",
      "dl.ttc.name": "TTC 集合包",
      "dl.ttc.note": "单文件集合，兼容旧版 WPS 与老系统。",
      "dl.woff2.name": "网页字体包",
      "dl.woff2.note": "网站嵌入用 WOFF2 压缩版本。",
      "dl.subset.name": "网页子集",
      "dl.subset.note": "页面常用字子集，线上页面优先使用。",
      "dl.demo.name": "演示极小集",
      "dl.demo.note": "极小子集，可直接嵌入轻量页面使用。",
      "dl.gh": "GitHub Release 全部版本",
      "dl.prompt.title": "给 AI 助手的自取提示词",
      "dl.prompt.sub": "每个安装包对应独立提示词，可直接复制给 AI 助手自取。",
      "dl.prompt.copy": "复制提示词",
      "dl.prompt.copied": "已复制",
      "dl.prompt.variable.body": "请从 GitHub 获取「柳皓升方润黑体 / HowsenLiu Fangrun」可变字体包，安装到我的项目。\n直达下载：https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-VF.zip\n仓库：https://github.com/HowsenLiu/HowsenLiuFangrun\n包内为可变字体 HowsenLiuFangrun-VF.ttf，含字重 wght 100–700、宽度 wdth 75–105、光学尺寸 opsz 12–72 三轴。\n按仓库 LICENSE（SIL OFL 1.1）授权使用：可免费商用，也允许修改与制作衍生字体；衍生版本须继续以 OFL 1.1 发布，并保留署名与许可文本；字体文件不得脱离软件单独售卖。",
      "dl.prompt.static.body": "请从 GitHub 获取「柳皓升方润黑体 / HowsenLiu Fangrun」静态字重包，安装到我的项目。\n直达下载：https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-Static-TTF.zip\n仓库：https://github.com/HowsenLiu/HowsenLiuFangrun\n包内含 Light / Regular / Medium / Bold 四款静态 TTF。\n按仓库 LICENSE（SIL OFL 1.1）授权使用：可免费商用，也允许修改与制作衍生字体；衍生版本须继续以 OFL 1.1 发布，并保留署名与许可文本；字体文件不得脱离软件单独售卖。",
      "dl.prompt.ttc.body": "请从 GitHub 获取「柳皓升方润黑体 / HowsenLiu Fangrun」TTC 集合包，安装到我的项目（兼容旧版 WPS 与老系统）。\n直达下载：https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-TTC.zip\n仓库：https://github.com/HowsenLiu/HowsenLiuFangrun\n包内为单文件 TTC 集合，一次装入四款静态字重。\n按仓库 LICENSE（SIL OFL 1.1）授权使用：可免费商用，也允许修改与制作衍生字体；衍生版本须继续以 OFL 1.1 发布，并保留署名与许可文本；字体文件不得脱离软件单独售卖。",
      "dl.prompt.woff2.body": "请从 GitHub 获取「柳皓升方润黑体 / HowsenLiu Fangrun」网页 WOFF2 包，嵌入我的网站。\n直达下载：https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-WOFF2.zip\n仓库：https://github.com/HowsenLiu/HowsenLiuFangrun\n包内为网站嵌入用 WOFF2 压缩版本。\n按仓库 LICENSE（SIL OFL 1.1）授权使用：可免费商用，也允许修改与制作衍生字体；衍生版本须继续以 OFL 1.1 发布，并保留署名与许可文本；字体文件不得脱离软件单独售卖。",
      "license.title": "授权说明",
      "license.body1": "本字体以 SIL Open Font License 1.1（OFL 1.1）发布，使用边界遵循协议原文：可免费用于个人与商业项目，允许修改字形、调整参数与制作衍生字体；衍生版本必须继续以 OFL 1.1 发布，并保留原始版权声明、作者署名与许可全文。字体文件不得脱离软件单独售卖。",
      "license.body2": "保留字体名：HowsenLiu Fangrun、柳皓升方润黑体、方润黑体、Fangrun；衍生修改版不得沿用以上任何名称，需更名后发布。完整版权声明与 OFL 许可文本随包 LICENSE 提供。",
      "license.tags.title": "本仓库附带的两份许可证",
      "license.tag1.t": "本字体发布版 · SIL OFL 1.1",
      "license.tag1.d": "随包附带的完整 OFL 1.1 许可文本与版权声明。",
      "license.tag1.link": "查看 LICENSE",
      "license.tag2.t": "上游保留源文件 · SIL OFL 1.1",
      "license.tag2.d": "仓库内保留的上游源文件原始 OFL 1.1 声明，详见许可文本。",
      "license.tag2.link": "查看上游许可文本",
      "license.scenes.title": "使用场景对照",
      "scenes.allow.t": "可直接使用",
      "scenes.allow.d": "印刷品（海报、包装、宣传册）、视频字幕与封面、网页字体加载、个人及企业商业物料、设计稿交付",
      "scenes.bundle.t": "可随附分发",
      "scenes.bundle.d": "随软件、项目或硬件捆绑分发；须保留署名与 OFL 全文",
      "scenes.caution.t": "建议书面确认",
      "scenes.caution.d": "嵌入 App / 小程序 / 游戏安装包内部分发；以字体字形为核心元素申请注册商标",
      "scenes.prohibit.t": "禁止",
      "scenes.prohibit.d": "将字体文件本身单独打包标价出售；删除或篡改原始版权声明与许可文本",
      "license.link": "查看完整授权文本（OFL 1.1）",
      "footer.free": "OFL 1.1 · 免费商用",
      "tab.zh": "简体中文",
      "tab.tw": "繁體中文",
      "tab.en": "English",
      "tab.ja": "日本語",
      "tab.ko": "한국어",
      "tab.la": "欧洲语言",
      "tab.sym": "符号"
    },
    en: {
      "nav.specimen": "Specimen",
      "nav.design": "Design",
      "nav.download": "Download",
      "nav.license": "License",
      "brand.cn": "柳皓升®方润黑体",
      "meta.title": "HowsenLiu Fangrun Typeface",
      "hero.eyebrow": "HowsenLiu Fangrun · Typeface 2.000",
      "manifesto.line": "Square in structure, soft at the terminals.",
      "manifesto.sub": "A sans for screen and print: a continuous weight axis, square structure and gentle details — one skeleton across scripts.",
      "stage.title": "Multilingual",
      "stage.sub": "Simplified · Traditional · English · Japanese · Korean · European · Symbols — one skeleton across scripts.",
      "weight.title": "Weight in Motion",
      "weight.sub": "One skeleton from thin to bold: only strokes thicken, fillet radius and proportions stay unchanged.",
      "ax.wght": "Weight",
      "ax.wdth": "Width",
      "ax.opsz": "Optical",
      "detail.title": "Design Language",
      "detail.macro": "Rounded terminals · one radius",
      "sheet.radius": "R · Unified fillet radius",
      "sheet.angle": "90° skeleton corner, filleted",
      "sheet.frame": "Em box 1000 × 1000",
      "glyph.title": "Character Coverage",
      "glyph.sub": "Common Han, Hangul, European accented letters and symbols, kana and numerals in one visual system.",
      "f1.t": "Unified Rounding",
      "f1.d": "Every corner and terminal shares one fillet radius, for one consistent and restrained voice.",
      "f2.t": "Wide Coverage",
      "f2.d": "44,731 glyphs / 44,828 code points: GBK, GB 18030 Levels 1–2, Big5, Hangul syllables and jamo, kana, bopomofo, Greek, Cyrillic, European accented letters and common symbols.",
      "f3.t": "Multiple Weights",
      "f3.d": "Variable weight 100–700, plus four static weights: Light / Regular / Medium / Bold.",
      "dl.title": "Download",
      "dl.sub": "Subsets download directly from this page; full packages and historical releases are on GitHub Release.",
      "dl.variable.name": "Variable Pack",
      "dl.variable.note": "Full variable package for desktop installation and design software.",
      "dl.static.name": "Static TTF",
      "dl.static.note": "Four static weights: Light / Regular / Medium / Bold.",
      "dl.ttc.name": "TTC Collection",
      "dl.ttc.note": "Single-file collection for legacy WPS and older systems.",
      "dl.woff2.name": "Web WOFF2",
      "dl.woff2.note": "Compressed WOFF2 builds for web embedding.",
      "dl.subset.name": "Web Subset",
      "dl.subset.note": "Common-glyph subset, preferred for live pages.",
      "dl.demo.name": "Demo Subset",
      "dl.demo.note": "Minimal subset, ready for lightweight web embedding.",
      "dl.gh": "All versions on GitHub Release",
      "dl.prompt.title": "AI self-serve prompt",
      "dl.prompt.sub": "One tailored prompt per package — copy the one you need for your AI assistant.",
      "dl.prompt.copy": "Copy prompt",
      "dl.prompt.copied": "Copied",
      "dl.prompt.variable.body": "Fetch the \"HowsenLiu Fangrun\" variable font pack from GitHub and install it in my project.\nDirect download: https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-VF.zip\nRepo: https://github.com/HowsenLiu/HowsenLiuFangrun\nThe pack contains HowsenLiuFangrun-VF.ttf, with axes wght 100–700, wdth 75–105 and opsz 12–72.\nUse it under the repository LICENSE (SIL OFL 1.1): free for commercial use; modification and derivatives are allowed, but derivatives must remain under OFL 1.1 with attribution and license text retained; the font files may not be sold standalone.",
      "dl.prompt.static.body": "Fetch the \"HowsenLiu Fangrun\" static TTF pack from GitHub and install it in my project.\nDirect download: https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-Static-TTF.zip\nRepo: https://github.com/HowsenLiu/HowsenLiuFangrun\nThe pack carries four static weights: Light / Regular / Medium / Bold.\nUse it under the repository LICENSE (SIL OFL 1.1): free for commercial use; modification and derivatives are allowed, but derivatives must remain under OFL 1.1 with attribution and license text retained; the font files may not be sold standalone.",
      "dl.prompt.ttc.body": "Fetch the \"HowsenLiu Fangrun\" TTC collection from GitHub and install it in my project (for legacy WPS and older systems).\nDirect download: https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-TTC.zip\nRepo: https://github.com/HowsenLiu/HowsenLiuFangrun\nSingle-file TTC collection with all four static weights.\nUse it under the repository LICENSE (SIL OFL 1.1): free for commercial use; modification and derivatives are allowed, but derivatives must remain under OFL 1.1 with attribution and license text retained; the font files may not be sold standalone.",
      "dl.prompt.woff2.body": "Fetch the \"HowsenLiu Fangrun\" web WOFF2 pack from GitHub and embed it in my website.\nDirect download: https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-WOFF2.zip\nRepo: https://github.com/HowsenLiu/HowsenLiuFangrun\nCompressed WOFF2 builds for web embedding.\nUse it under the repository LICENSE (SIL OFL 1.1): free for commercial use; modification and derivatives are allowed, but derivatives must remain under OFL 1.1 with attribution and license text retained; the font files may not be sold standalone.",
      "license.title": "License",
      "license.body1": "Released under the SIL Open Font License 1.1 (OFL 1.1). Usage follows the OFL 1.1 text: free for personal and commercial use; glyphs may be modified and derivative fonts may be created. Derivatives must remain under OFL 1.1 and retain the original copyright notices, author attribution and full license text. The font files may not be sold standalone.",
      "license.body2": "Reserved Font Names: HowsenLiu Fangrun, 柳皓升方润黑体, 方润黑体, Fangrun. Modified derivatives must be renamed and may not keep any of these names. Full copyright notices and the OFL license text ship in the package LICENSE.",
      "license.tags.title": "Two OFL 1.1 texts in this repository",
      "license.tag1.t": "This release · SIL OFL 1.1",
      "license.tag1.d": "Full OFL 1.1 license text and copyright notices shipped with the package.",
      "license.tag1.link": "Read LICENSE",
      "license.tag2.t": "Retained upstream source · SIL OFL 1.1",
      "license.tag2.d": "Verbatim OFL 1.1 notice retained for the upstream source file; see the license text.",
      "license.tag2.link": "Read upstream license",
      "license.scenes.title": "Usage scenarios",
      "scenes.allow.t": "Allowed",
      "scenes.allow.d": "Print (posters, packaging, brochures), video subtitles and covers, web font loading, personal and commercial brand materials, design deliverables",
      "scenes.bundle.t": "Redistributable",
      "scenes.bundle.d": "Bundling with software, projects or hardware; keep attribution and the full OFL text",
      "scenes.caution.t": "Confirm in writing",
      "scenes.caution.d": "Embedding inside App / mini-program / game install packages; registering trademarks built primarily on the glyph shapes",
      "scenes.prohibit.t": "Prohibited",
      "scenes.prohibit.d": "Selling the font files standalone as a package; removing or altering the original copyright notices and license text",
      "license.link": "Read the full license text (OFL 1.1)",
      "footer.free": "OFL 1.1 · Free for commercial use",
      "tab.zh": "Simplified",
      "tab.tw": "Traditional",
      "tab.en": "English",
      "tab.ja": "Japanese",
      "tab.ko": "Korean",
      "tab.la": "European",
      "tab.sym": "Symbols"
    }
  };

  const root = document.documentElement;
  let lang = localStorage.getItem("hfl-lang") || "zh";

  const PROMPT_PACKAGES = [
    { key: "variable", nameKey: "dl.variable.name", file: "HowsenLiuFangrun-VF.zip",
      url: "https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-VF.zip" },
    { key: "static", nameKey: "dl.static.name", file: "HowsenLiuFangrun-Static-TTF.zip",
      url: "https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-Static-TTF.zip" },
    { key: "ttc", nameKey: "dl.ttc.name", file: "HowsenLiuFangrun-TTC.zip",
      url: "https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-TTC.zip" },
    { key: "woff2", nameKey: "dl.woff2.name", file: "HowsenLiuFangrun-WOFF2.zip",
      url: "https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-WOFF2.zip" }
  ];

  function renderPrompts() {
    const list = document.getElementById("promptList");
    if (!list) return;
    list.innerHTML = "";
    PROMPT_PACKAGES.forEach(function (p) {
      const item = document.createElement("div");
      item.className = "dl-prompt-item";

      const head = document.createElement("div");
      head.className = "dl-prompt-item-head";
      const title = document.createElement("div");
      title.className = "dl-prompt-item-title";
      const b = document.createElement("b");
      b.setAttribute("data-i18n", p.nameKey);
      b.textContent = I18N[lang][p.nameKey] || "";
      const file = document.createElement("span");
      file.className = "dl-prompt-file";
      file.textContent = p.file;
      title.appendChild(b);
      title.appendChild(file);

      const btn = document.createElement("button");
      btn.className = "copy-btn";
      btn.type = "button";
      btn.setAttribute("data-copy", p.key);
      btn.textContent = I18N[lang]["dl.prompt.copy"];
      head.appendChild(title);
      head.appendChild(btn);

      const url = document.createElement("a");
      url.className = "dl-prompt-url";
      url.href = p.url;
      url.target = "_blank";
      url.rel = "noopener";
      url.textContent = p.url;

      const pre = document.createElement("pre");
      pre.className = "dl-prompt-code";
      const code = document.createElement("code");
      code.setAttribute("data-prompt-body", p.key);
      code.textContent = I18N[lang]["dl.prompt." + p.key + ".body"] || "";
      pre.appendChild(code);

      item.appendChild(head);
      item.appendChild(url);
      item.appendChild(pre);
      list.appendChild(item);
    });
  }

  function applyLang() {
    const dict = I18N[lang];
    root.setAttribute("lang", lang === "en" ? "en" : "zh-CN");
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      const key = el.getAttribute("data-i18n");
      if (dict[key]) el.textContent = dict[key];
    });
    if (dict["meta.title"]) document.title = dict["meta.title"];
    document.querySelectorAll("[data-prompt-body]").forEach(function (el) {
      const k = el.getAttribute("data-prompt-body");
      const t = dict["dl.prompt." + k + ".body"];
      if (t) el.textContent = t;
    });
    document.querySelectorAll("[data-copy]").forEach(function (btn) {
      btn.textContent = dict["dl.prompt.copy"];
    });
  }

  const navBurger = document.getElementById("navBurger");
  const navLinks = document.getElementById("navLinks");
  const navBar = document.getElementById("nav");
  if (navBurger && navLinks && navBar) {
    const setMenu = function (open) {
      navBar.classList.toggle("nav-open", open);
      navBurger.setAttribute("aria-expanded", open ? "true" : "false");
      navBurger.setAttribute("aria-label", open ? "关闭菜单" : "打开菜单");
    };
    navBurger.addEventListener("click", function () {
      setMenu(!navBar.classList.contains("nav-open"));
    });
    navLinks.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { setMenu(false); });
    });
    document.addEventListener("click", function (e) {
      if (navBar.classList.contains("nav-open") && !navBar.contains(e.target)) setMenu(false);
    });
  }

  const langToggle = document.getElementById("langToggle");
  if (langToggle) {
    langToggle.addEventListener("click", function () {
      lang = lang === "zh" ? "en" : "zh";
      localStorage.setItem("hfl-lang", lang);
      applyLang();
      if (wallRefresh) wallRefresh();
    });
  }
  renderPrompts();
  applyLang();

  const promptList = document.getElementById("promptList");
  if (promptList) {
    promptList.addEventListener("click", function (e) {
      const btn = e.target.closest("[data-copy]");
      if (!btn) return;
      const key = btn.getAttribute("data-copy");
      const box = promptList.querySelector('[data-prompt-body="' + key + '"]');
      const text = box ? box.textContent : "";
      const done = function () {
        btn.textContent = I18N[lang]["dl.prompt.copied"];
        setTimeout(function () {
          btn.textContent = I18N[lang]["dl.prompt.copy"];
        }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, done);
      } else {
        done();
      }
    });
  }

  const reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------------------------------------------------- 首屏大字轮播（苹果激活式） */
  const HERO_WORDS = [
    { word: "柳皓升®方润黑体", caption: "简体中文 · Simplified Chinese" },
    { word: "HowsenLiuFangrun", caption: "English" },
    { word: "柳皓升方潤黑體", caption: "繁體中文 · Traditional Chinese" },
    { word: "柳皓升方潤ゴシック", caption: "日本語 · Japanese" },
    { word: "柳皓升방운고딕", caption: "한국어 · Korean" },
    { word: "HöwsënLiú Fängrün", caption: "European · 欧洲语言" },
    { word: "，。！？·★○●", caption: "Symbols · Punctuation" }
  ];

  const heroWord = document.getElementById("heroWord");
  const heroCaption = document.getElementById("heroCaption");
  const heroStage = document.getElementById("heroStage");
  let heroIdx = 0;
  let heroTimer = null;

  function renderHeroChars(word) {
    heroWord.textContent = "";
    Array.from(word).forEach(function (ch, i) {
      const span = document.createElement("span");
      span.className = "hchar";
      span.style.setProperty("--i", i);
      span.textContent = ch === " " ? " " : ch;
      heroWord.appendChild(span);
    });
  }

  function writeHero(i) {
    const item = HERO_WORDS[i];
    heroCaption.textContent = item.caption;
    renderHeroChars(item.word);
    if (reduced) return;
    heroWord.classList.remove("writing");
    void heroWord.offsetWidth;
    heroWord.classList.add("writing");
  }

  function rotateHero() {
    if (!heroWord) return;
    if (reduced) { heroIdx = (heroIdx + 1) % HERO_WORDS.length; writeHero(heroIdx); return; }
    heroWord.classList.add("swap-out");
    heroCaption.classList.add("swap-out");
    setTimeout(function () {
      heroIdx = (heroIdx + 1) % HERO_WORDS.length;
      writeHero(heroIdx);
      heroWord.classList.remove("swap-out");
      heroCaption.classList.remove("swap-out");
      setTimeout(function () { heroCaption.classList.add("swap-in"); }, 120);
      setTimeout(function () { heroCaption.classList.remove("swap-in"); }, 700);
    }, 520);
  }

  if (heroWord) {
    writeHero(0);
    if (!reduced) heroTimer = setInterval(rotateHero, 4600);
  }

  /* 首屏轻微视差（指针驱动，触屏与降级模式关闭） */
  if (heroStage && !reduced && window.matchMedia("(pointer: fine)").matches) {
    heroStage.addEventListener("mousemove", function (e) {
      const r = heroStage.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - 0.5;
      const y = (e.clientY - r.top) / r.height - 0.5;
      heroStage.style.transform = "translate3d(" + (x * 14) + "px," + (y * 10) + "px,0)";
    });
    heroStage.addEventListener("mouseleave", function () {
      heroStage.style.transform = "translate3d(0,0,0)";
    });
  }

  /* ---------------------------------------------------------- 语言舞台 */
  const panels = Array.prototype.slice.call(document.querySelectorAll(".lpanel"));
  const tabs = Array.prototype.slice.call(document.querySelectorAll(".tab"));
  const dotsBox = document.getElementById("dots");
  let current = 0;
  let carTimer = null;

  panels.forEach(function (_, i) {
    const dot = document.createElement("button");
    dot.className = "dot" + (i === 0 ? " active" : "");
    dot.type = "button";
    dot.setAttribute("aria-label", "第 " + (i + 1) + " 组样张");
    dot.addEventListener("click", function () { go(i); restart(); });
    dotsBox.appendChild(dot);
  });
  const dots = Array.prototype.slice.call(dotsBox.children);

  /* 面板标题逐字拆分，复用首屏手写感入场；欧洲语言面板保留随机轮换，不拆字 */
  function paintPanel(panel) {
    if (!panel || panel.dataset.panel === "la") return;
    ["lpanel-big", "lpanel-sub"].forEach(function (cls) {
      const el = panel.querySelector("." + cls);
      if (!el) return;
      if (!el.dataset.raw) el.dataset.raw = el.textContent;
      const text = el.dataset.raw;
      el.textContent = "";
      Array.from(text).forEach(function (ch, i) {
        const sp = document.createElement("span");
        sp.className = "hchar";
        sp.style.setProperty("--i", i);
        sp.textContent = ch === " " ? " " : ch;
        el.appendChild(sp);
      });
    });
    panel.classList.remove("writing");
    void panel.offsetWidth;
    panel.classList.add("writing");
  }

  function go(i) {
    current = (i + panels.length) % panels.length;
    panels.forEach(function (p, k) { p.classList.toggle("active", k === current); });
    tabs.forEach(function (t, k) {
      t.classList.toggle("active", k === current);
      t.setAttribute("aria-selected", k === current ? "true" : "false");
    });
    dots.forEach(function (d, k) { d.classList.toggle("active", k === current); });
    paintPanel(panels[current]);
    if (panels[current].dataset.panel === "la") { euStart(); } else { euStop(); }
  }

  tabs.forEach(function (t) {
    t.addEventListener("click", function () { go(tabs.indexOf(t)); restart(); });
  });

  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  if (prevBtn) prevBtn.addEventListener("click", function () { go(current - 1); restart(); });
  if (nextBtn) nextBtn.addEventListener("click", function () { go(current + 1); restart(); });

  function restart() {
    if (carTimer) clearInterval(carTimer);
    if (!reduced) carTimer = setInterval(function () { go(current + 1); }, 6000);
  }

  const stage = document.getElementById("langPanels");
  if (stage) {
    stage.addEventListener("mouseenter", function () { if (carTimer) clearInterval(carTimer); });
    stage.addEventListener("mouseleave", restart);
  }
  restart();

  /* 触摸滑动 */
  let touchX = null;
  if (stage) {
    stage.addEventListener("touchstart", function (e) { touchX = e.touches[0].clientX; }, { passive: true });
    stage.addEventListener("touchend", function (e) {
      if (touchX === null) return;
      const dx = e.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 48) { go(dx < 0 ? current + 1 : current - 1); restart(); }
      touchX = null;
    }, { passive: true });
  }

  /* ---------------------------------------------------------- 欧洲语言：元音变音随机轮换 */
  const EU_BASE = "HowsenLiu Fangrun";
  const EU_SUBS = ["HowsenLiu Fangrun", "HöwsënLiú Fängrün", "HowsenLiú Fàngrùn"];
  const EU_VOWELS = {
    a: "aàáǎâãäāå", A: "AÀÁÂÃÄÅĀ",
    e: "eèéěêëē", E: "EÈÉÊËĒ",
    i: "iìíǐîïī", I: "IÌÍÎÏĪ",
    o: "oòóǒôõöōø", O: "OÒÓÔÕÖŌØ",
    u: "uùúǔûüū", U: "UÙÚÛÜŪ"
  };
  let euBigTimer = null, euSubTimer = null, euSubIdx = 0;

  function euRandomize() {
    const big = document.getElementById("euBig");
    if (!big) return;
    let out = "";
    for (let i = 0; i < EU_BASE.length; i++) {
      const family = EU_VOWELS[EU_BASE[i]];
      out += family ? family[Math.floor(Math.random() * family.length)] : EU_BASE[i];
    }
    big.textContent = out;
  }

  function euStart() {
    euStop();
    if (reduced) return;
    euRandomize();
    euBigTimer = setInterval(euRandomize, 1800);
    const sub = document.getElementById("euSub");
    if (sub) {
      euSubTimer = setInterval(function () {
        euSubIdx = (euSubIdx + 1) % EU_SUBS.length;
        sub.textContent = EU_SUBS[euSubIdx];
      }, 2400);
    }
  }

  function euStop() {
    if (euBigTimer) clearInterval(euBigTimer);
    if (euSubTimer) clearInterval(euSubTimer);
    euBigTimer = euSubTimer = null;
  }

  const activeIdx = panels.findIndex(function (p) { return p.classList.contains("active"); });
  paintPanel(panels[activeIdx]);
  if (panels[activeIdx].dataset.panel === "la") euStart();

  /* ---------------------------------------------------------- 字重大框：可变轴全站实时调控 */
  const weightStage = document.querySelector(".weight-stage");
  if (weightStage) {
    const sliders = Array.prototype.slice.call(weightStage.querySelectorAll("input[data-axis]"));

    function applyWeight() {
      const vals = {};
      sliders.forEach(function (s) {
        vals[s.dataset.axis] = s.value;
        const out = weightStage.querySelector('[data-val="' + s.dataset.axis + '"]');
        if (out) out.textContent = s.value;
      });
      // 写到根元素，全站使用该字体的文字随三轴一起变化
      document.documentElement.style.fontVariationSettings =
        '"wght" ' + vals.wght + ', "wdth" ' + vals.wdth + ', "opsz" ' + vals.opsz;
    }

    sliders.forEach(function (s) { s.addEventListener("input", applyWeight); });

    applyWeight();
  }

  /* ---------------------------------------------------------- 字符墙：分组快速轮换 */
  const glyphWall = document.getElementById("glyphWall");
  const glyphGroup = document.getElementById("glyphGroup");
  let wallRefresh = null;
  if (glyphWall) {
    const GROUPS = [
      { zh: "简体中文", en: "Simplified Han", chars: "柳皓升方润黑体圆角骨架温润如玉端正谦和安宁稳重简约现代清晰" },
      { zh: "繁體中文", en: "Traditional Han", chars: "柳皓升方潤黑體圓角骨架溫潤如玉端正謙和安寧穩重簡約現代清晰" },
      { zh: "Latin 字母", en: "Latin", chars: "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" },
      { zh: "欧洲语言", en: "European", chars: "ÀÁÂÃÄÅÆÇÈÉÊËÑÓÔÕÖÚÜßàáâãäåæçèéêëìíîïñòóôõöøùúûüýþÿœ" },
      { zh: "日文假名", en: "Kana", chars: "あいうえおかきくけこさしすせそたちつてとなにぬねのアイウエオカキクケコサシスセソタチツテト" },
      { zh: "韩文谚文", en: "Hangul", chars: "가나다라마바사아자차카타파하글로벌한국어폰트설계" },
      { zh: "数字与罗马数字", en: "Numerals", chars: "0123456789ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ" },
      { zh: "标点符号", en: "Symbols", chars: "，。！？·★○●◆◇※→←↑↓№§" }
    ];
    const CELLS = 36;
    const cells = [];
    for (let i = 0; i < CELLS; i++) {
      const s = document.createElement("span");
      s.style.transitionDelay = (i * 16) + "ms";
      glyphWall.appendChild(s);
      cells.push(s);
    }
    let gi = 0;

    function fillGroup() {
      const g = GROUPS[gi];
      if (glyphGroup) glyphGroup.textContent = g[lang];
      cells.forEach(function (el, i) {
        el.classList.add("flipping");
        setTimeout(function () {
          el.textContent = g.chars[i % g.chars.length];
          el.classList.remove("flipping");
        }, 110 + i * 16);
      });
    }

    wallRefresh = fillGroup;
    fillGroup();

    if ("IntersectionObserver" in window && !reduced) {
      const wallIO = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            glyphWall.classList.add("in");
            wallIO.disconnect();
          }
        });
      }, { threshold: 0.15 });
      wallIO.observe(glyphWall);
    } else {
      glyphWall.classList.add("in");
    }

    setInterval(function () {
      gi = (gi + 1) % GROUPS.length;
      fillGroup();
    }, 2400);
  }

  /* ---------------------------------------------------------- 滚动入场 */
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduced) {
    const io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }
})();
