#app-refresh.app-refresh(style='position: fixed;top: -2.2rem;left: 0;right: 0;z-index: 99999;padding: 0 1rem;font-size: 15px;height: 2.2rem;transition: all 0.3s ease;')
  .app-refresh-wrap(style=' display: flex;color: #fff;height: 100%;align-items: center;justify-content: center;')
    label ✨ 兼一书虫上新啦！ 👉
    a(href='javascript:void(0)' onclick='location.reload()')
      span(style='color: #fff;text-decoration: underline;cursor: pointer;') 🍭查看新品🍬
script.
  if ('serviceWorker' in navigator) {
  if (navigator.serviceWorker.controller) {
  navigator.serviceWorker.addEventListener('controllerchange', function() {
  showNotification()
  })
  }
  window.addEventListener('load', function() {
  navigator.serviceWorker.register('/sw.js')
  })
  }
  function showNotification() {
  if (GLOBAL_CONFIG.Snackbar) {
  var snackbarBg =
  document.documentElement.getAttribute('data-theme') === 'light' ?
  GLOBAL_CONFIG.Snackbar.bgLight :
  GLOBAL_CONFIG.Snackbar.bgDark
  var snackbarPos = GLOBAL_CONFIG.Snackbar.position
  Snackbar.show({
  text: '✨ 糖果屋上新啦！ 👉',
  backgroundColor: snackbarBg,
  duration: 500000,
  pos: snackbarPos,
  actionText: '🍭查看新品🍬',
  actionTextColor: '#fff',
  onActionClick: function(e) {
  location.reload()
  },
  })
  } else {
  var showBg =
  document.documentElement.getAttribute('data-theme') === 'light' ?
  '#49b1f5' :
  '#1f1f1f'
  var cssText = `top: 0; background: ${showBg};`
  document.getElementById('app-refresh').style.cssText = cssText
  }
  }