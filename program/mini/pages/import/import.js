const db = wx.cloud.database(); 

Page({
  data: {
    originalText: '',
    kana: '',
    meaning: '',
    note: '',
    isEdit: false,  // 是否为编辑模式
    editId: ''      // 编辑的单词ID
  },

  onLoad(options) {
    // 检查是否是编辑模式（有editId参数）
    if (options.editId) {
      this.setData({
        isEdit: true,
        editId: options.editId,
        // 解码URL参数并赋值（处理特殊字符）
        originalText: decodeURIComponent(options.originalText || ''),
        kana: decodeURIComponent(options.kana || ''),
        meaning: decodeURIComponent(options.meaning || ''),
        note: decodeURIComponent(options.note || '')
      });
    }
  },

  // 输入框事件处理
  handleOriginalInput(e) {
    this.setData({ originalText: e.detail.value })
  },
  handleKanaInput(e) {
    this.setData({ kana: e.detail.value })
  },
  handleMeaningInput(e) {
    this.setData({ meaning: e.detail.value })
  },
  handleNoteInput(e) {
    this.setData({ note: e.detail.value })
  },

  // 保存单词（新增或编辑）
  saveItem() {
    // 验证必填项
    if (!this.data.originalText.trim()) {
      wx.showToast({ title: '请输入日语原文', icon: 'none' })
      return;
    }

    if (this.data.isEdit) {
      // 编辑模式：更新现有单词
      db.collection('japanese_items')
        .doc(this.data.editId)
        .update({
          data: {
            originalText: this.data.originalText.trim(),
            kana: this.data.kana.trim(),
            meaning: this.data.meaning.trim(),
            note: this.data.note.trim()
          }
        })
        .then(res => {
          wx.showToast({ title: '修改成功', icon: 'success' })
          // 返回单词库页面
          setTimeout(() => {
            wx.navigateBack();
          }, 1000);
        })
        .catch(err => {
          wx.showToast({ title: '修改失败', icon: 'none' })
          console.error(err)
        })
    } else {
      // 新增模式：添加新单词
      db.collection('japanese_items').add({
        data: {
          originalText: this.data.originalText.trim(),
          kana: this.data.kana.trim(),
          meaning: this.data.meaning.trim(),
          note: this.data.note.trim(),
          createTime: new Date().getTime(),
          level: 0,
          nextReviewTime: new Date().getTime() + 24 * 60 * 60 * 1000
        }
      }).then(res => {
        wx.showToast({ title: '添加成功', icon: 'success' })
        // 清空输入框
        this.setData({ originalText: '', kana: '', meaning: '', note: '' })
      }).catch(err => {
        wx.showToast({ title: '添加失败', icon: 'none' })
        console.error(err)
      })
    }
  },

  // 取消编辑，返回单词库
  cancelEdit() {
    wx.navigateBack();
  }
})
    