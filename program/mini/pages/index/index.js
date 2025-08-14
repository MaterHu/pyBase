// pages/index/index.js
Page({
  data: {
    // 页面数据（暂时为空）
  },

  // 跳转到导入页
  goToImport() {
    wx.navigateTo({
      url: '/pages/import/import'
    });
  },

  // 跳转到仓库页
  goToRepository() {
    wx.navigateTo({
      url: '/pages/repository/repository'
    });
  },

  // 跳转到复习页
  goToReview() {
    wx.navigateTo({
      url: '/pages/review/review'
    });
  },

  // 以下是默认生命周期函数（保持不变）
  onLoad(options) {},
  onReady() {},
  onShow() {},
  onHide() {},
  onUnload() {},
  onPullDownRefresh() {},
  onReachBottom() {},
  onShareAppMessage() {}
})