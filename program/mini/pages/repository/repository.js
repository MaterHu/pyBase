const db = wx.cloud.database();

Page({
  data: {
    items: [], // 单词列表数据
    startX: 0, // 触摸起始X坐标
    currentIndex: -1, // 当前滑动的索引
    buttonWidth: 240, // 两个按钮总宽度（rpx）
  },

  onLoad() {
    this.loadWordList();
  },

  onShow() {
    // 返回页面时重新加载数据
    this.loadWordList();
  },

  // 跳转到添加单词页
  goToImport() {
    wx.navigateTo({
      url: '/pages/import/import'
    });
  },

  // 加载单词列表
  loadWordList() {
    db.collection('japanese_items')
      .get()
      .then(res => {
        // 初始化每个单词的滑动偏移量
        const items = res.data.map(item => ({
          ...item,
          swipeOffset: 0 // 初始偏移为0（不滑动）
        }));
        this.setData({ items });
      })
      .catch(err => {
        console.error('加载单词失败：', err);
        wx.showToast({ title: '加载失败', icon: 'none' });
      });
  },

  // 触摸开始
  touchStart(e) {
    const index = e.currentTarget.dataset.index;
    this.setData({
      startX: e.touches[0].clientX,
      currentIndex: index
    });
  },

  // 触摸移动
  touchMove(e) {
    const currentIndex = this.data.currentIndex;
    if (currentIndex === -1) return;

    const moveX = e.touches[0].clientX;
    const startX = this.data.startX;
    let offset = startX - moveX; // 计算偏移量

    // 限制偏移范围：0到-240rpx（按钮总宽度）
    if (offset <= 0) offset = 0;
    if (offset >= this.data.buttonWidth) offset = this.data.buttonWidth;

    // 更新当前项的偏移量
    const items = this.data.items;
    items[currentIndex].swipeOffset = -offset;
    this.setData({ items });
  },

  // 触摸结束
  touchEnd() {
    const currentIndex = this.data.currentIndex;
    if (currentIndex === -1) return;

    const items = this.data.items;
    const currentOffset = Math.abs(items[currentIndex].swipeOffset);

    // 判断滑动距离是否超过按钮宽度的一半，决定是否展开
    if (currentOffset > this.data.buttonWidth / 2) {
      items[currentIndex].swipeOffset = -this.data.buttonWidth;
    } else {
      items[currentIndex].swipeOffset = 0;
    }

    this.setData({ items, currentIndex: -1 });
  },

  // 编辑单词
  editItem(e) {
    const id = e.currentTarget.dataset.id;
    const item = this.data.items.find(item => item._id === id);

    if (!item) return;

    // 跳转到导入页并携带参数（编码特殊字符）
    wx.navigateTo({
      url: `/pages/import/import?` +
        `editId=${id}&` +
        `originalText=${encodeURIComponent(item.originalText)}&` +
        `kana=${encodeURIComponent(item.kana || '')}&` +
        `meaning=${encodeURIComponent(item.meaning || '')}&` +
        `note=${encodeURIComponent(item.note || '')}`
    });
  },

  // 删除单词
  deleteItem(e) {
    const id = e.currentTarget.dataset.id;
    const index = e.currentTarget.dataset.index;

    wx.showModal({
      title: '确认删除',
      content: '确定要删除这个单词吗？',
      cancelText: '取消',
      confirmText: '删除',
      success: res => {
        if (res.confirm) {
          db.collection('japanese_items')
            .doc(id)
            .remove()
            .then(() => {
              // 删除成功后更新列表
              const items = this.data.items;
              items.splice(index, 1);
              this.setData({ items });
              wx.showToast({ title: '删除成功' });
            })
            .catch(err => {
              console.error('删除失败：', err);
              wx.showToast({ title: '删除失败', icon: 'none' });
            });
        }
      }
    });
  }
});
