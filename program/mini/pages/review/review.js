const db = wx.cloud.database(); 
const _ = db.command; // 数据库操作符（用于条件查询）

Page({
  data: {
    isLoading: true, // 新增：加载状态（初始为true）
    reviewList: [],   // 待复习单词列表
    currentItem: {},  // 当前显示的单词
    currentIndex: 0,   // 当前单词在列表中的索引
    cardAnimation: {} // 新增：动画对象
  },

  onLoad() {
    // 开始加载（可省略，因为data中已初始化为true）
    this.setData({ isLoading: true });

    // 1. 查询需要复习的单词：nextReviewTime ≤ 当前时间
    db.collection('japanese_items')
      .where({
        nextReviewTime: _.lte(new Date().getTime())
      })
      .get()
      .then(res => {
        this.setData({ 
          reviewList: res.data,
          currentItem: res.data[0] || {},
          isLoading: false // 新增：请求成功后关闭加载 
        });
      })
      .catch(err => {
        wx.showToast({ title: '加载失败', icon: 'none' });
        this.setData({ isLoading: false }); // 新增：请求失败也关闭加载
        console.error(err);
      });
  },

  // 操作：认识（提升记忆等级，延长复习间隔）
  handleKnow() {
    this.updateReviewLevel(1); // 等级 +1
  },

  // 操作：不认识（重置记忆等级，缩短复习间隔）
  handleUnknown() {
    this.updateReviewLevel(0); // 等级重置
  },

  // 通用更新逻辑
  updateReviewLevel(isKnow) {
    const { reviewList, currentIndex } = this.data;
    const item = reviewList[currentIndex];

    // 根据操作更新记忆等级和下次复习时间
    let newLevel = item.level;
    let newReviewTime = new Date().getTime();

    if (isKnow) {
      newLevel += 1; // 认识：等级 +1
      // 复习间隔：按记忆曲线递增（这里简单模拟，可优化）
      newReviewTime += [1, 3, 7, 15, 30][newLevel] * 24 * 60 * 60 * 1000; 
    } else {
      newLevel = 0; // 不认识：等级重置为 0
      newReviewTime += 1 * 24 * 60 * 60 * 1000; // 1 天后复习
    }

    // 更新数据库
    db.collection('japanese_items')
      .doc(item._id)
      .update({
        data: {
          level: newLevel,
          nextReviewTime: newReviewTime
        }
      })
      .then(res => {
        wx.showToast({ title: '更新成功', icon: 'success' });
        // 切换到下一个单词
        this.nextItem();
      })
      .catch(err => {
        wx.showToast({ title: '更新失败', icon: 'none' });
        console.error(err);
      });
  },

  // 切换到下一个单词
  nextItem() {
    // 1. 先执行“渐隐”动画
    const animationOut = wx.createAnimation({
      duration: 300, // 动画时长300毫秒
      timingFunction: 'ease-out' // 缓动效果
    });
    animationOut.opacity(0).step(); // 透明度从1→0
    this.setData({ cardAnimation: animationOut.export() });
  
    // 2. 延迟300毫秒（等渐隐动画结束），执行“渐显”动画并切换单词
    setTimeout(() => {
      // 检查是否有下一个单词
      if (this.data.currentIndex + 1 < this.data.reviewList.length) {
        // 有下一个单词：更新索引和当前单词
        const animationIn = wx.createAnimation({
          duration: 300,
          timingFunction: 'ease-in'
        });
        animationIn.opacity(1).step(); // 透明度从0→1
  
        this.setData({
          currentIndex: this.data.currentIndex + 1,
          currentItem: this.data.reviewList[this.data.currentIndex + 1],
          cardAnimation: animationIn.export() // 应用渐显动画
        });
      } else {
        // 没有下一个单词：清空当前显示，提示完成
        this.setData({ currentItem: {} });
        wx.showToast({ title: '今日复习完成！', icon: 'success' });
      }
    }, 300); // 和动画时长保持一致
    }
  }
,);