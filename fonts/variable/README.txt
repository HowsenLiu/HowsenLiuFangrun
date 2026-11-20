HowsenLiuFangrun-VF.ttf 约 140 MB，超过 GitHub 单文件 100 MB 上限，
因此不作为仓库文件提交，而是挂在 Release 附件里：

    https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest

需要直链时可复制 Release 附件地址。
若一定要放进仓库，请开启 Git LFS 后单独提交：

    git lfs track "*.ttf"
    git add fonts/variable/HowsenLiuFangrun-VF.ttf
