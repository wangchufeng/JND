module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  devServer: {
    proxy: { // 为接口配置代理，解决跨域
      '/server/': {
        'target': 'http://127.0.0.1:22027/', //接口地址
        'secure': false, // false为http访问，true为https访问
        'changeOrigin': true, // 跨域访问设置，true代表跨域
        'pathRewrite': { // 路径改写规则
          '^/server': '' // 以/server/为开头的改写为''
        }
      }
    }
  }
}