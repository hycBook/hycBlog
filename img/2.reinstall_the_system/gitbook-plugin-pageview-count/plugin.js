var gitbook = window.gitbook;

/*
免費網站計數器 mfwzjsq.com - 為您的網站提供來訪人數統計服務。簡易的圖片顯示形式，純HTML程式碼有利於網頁快速加載。有123種豐富的圖形樣式可供選擇，以便搭配不同風格的網頁。

https://www.cutercounter.com

使用幫助
第一步：簡單的表格填空。
第二步：選擇計數器樣式。
第三步：點擊“獲取計數器程式碼”按鈕。
第四步：複製程式碼加入您網頁原始檔案的<body></body>内。

注意事項
①：拒絕一切非法網站使用本站服務。
②：請正確填寫您的網站地址，一個帳號僅可以在一個網站中使用，以便區分是否有惡意使用的情况。
③：關於演示。任意選擇一款樣式，演示中的計數器樣式會隨之改變。將滑鼠懸停在彩色小方格上，即可看到不同樣式的計數器在不同背景色中的顯示效果。
④：計數器程式碼中的變數舉例說明。例如id=srmuux&nd=6&style=1，其中，id=srmuux為帳號名，不可更改；nd=6為最少顯示位數，6可在1-9之間改動；style=1為計數器樣式代號，1可在1~123之間選擇變換。
⑤：計數器程式碼裏的連結是本站提供免費服務的基礎，不可删除，除非在您網站的首頁添加本站連結，程式碼為：
<a href="https://www.mfwzjsq.com/">免費網站計數器</a>。

隱私政策
一：本站會記錄您的訪問來路、訪問次數、訪問設備、IP地址等，以供統計分析使用，這是作為一款計數器應用的基本功能。
二：本站使用Cookies作為部分資訊傳輸的載體，以便更好地提供上述服務，請知悉。
三：關於協力廠商Cookies。您可能在本站看到Google提供的廣告，有可能使用了Cookies。瞭解更多穀歌廣告的隱私政策點擊這裡。您也可以使用Google廣告設定管理您看到的Google廣告。

*/

var iconSVg = '<svg t="1543310294340" \
            class="icon" style="" viewBox="0 0 1024 1024" version="1.1" \
            xmlns="http://www.w3.org/2000/svg" p-id="1104" xmlns:xlink="http://www.w3.org/1999/xlink" width="14" height="14"><defs><style type="text/css"></style></defs>\
            <path d="M512 416a96 96 0 1 0 0 192 96 96 0 0 0 0-192z m511.952 102.064c-0.016-0.448-0.064-0.864-0.096-1.296a8.16 8.16 0 0 0-0.08-0.656c0-0.32-0.064-0.624-0.128-0.928-0.032-0.368-0.064-0.736-0.128-1.088-0.032-0.048-0.032-0.096-0.032-0.144a39.488 39.488 0 0 0-10.704-21.536c-32.672-39.616-71.536-74.88-111.04-107.072-85.088-69.392-182.432-127.424-289.856-150.8-62.112-13.504-124.576-14.064-187.008-2.64-56.784 10.384-111.504 32-162.72 58.784-80.176 41.92-153.392 99.696-217.184 164.48-11.808 11.984-23.552 24.224-34.288 37.248-14.288 17.328-14.288 37.872 0 55.216 32.672 39.616 71.52 74.848 111.04 107.056 85.12 69.392 182.448 127.408 289.888 150.784 62.096 13.504 124.608 14.096 187.008 2.656 56.768-10.4 111.488-32 162.736-58.768 80.176-41.936 153.376-99.696 217.184-164.48 11.792-12 23.536-24.224 34.288-37.248 5.712-5.872 9.456-13.44 10.704-21.568l0.032-0.128a12.592 12.592 0 0 0 0.128-1.088c0.064-0.304 0.096-0.624 0.128-0.928l0.08-0.656 0.096-1.28c0.032-0.656 0.048-1.296 0.048-1.952l-0.096-1.968zM512 704c-106.032 0-192-85.952-192-192s85.952-192 192-192 192 85.968 192 192c0 106.048-85.968 192-192 192z"\
            fill="#CCC" p-id="1105"></path></svg>'


// 配置 https://www.cutercounter.com/
// 设置风格编号
var counter_style = '109'
// 配置各网页id
var id_map = new Map();
// https://hycbook.github.io/bk_index/
id_map.set("", "hxappko");
// https://hycbook.github.io/bk_index/chapters/1.alicloud_deployment.html
id_map.set("1.alicloud_deployment.html", "hvxappkp");
// https://hycbook.github.io/bk_index/chapters/2.reinstall_the_system.html
id_map.set("2.reinstall_the_system.html", "huxappkq");
// https://hycbook.github.io/bk_index/chapters/3.Linux常用命令.html
id_map.set("3.Linux常用命令.html", "hexappkc");
// https://hycbook.github.io/bk_index/chapters/4.github协作.html
id_map.set("4.github协作.html", "huuxappax");
// https://hycbook.github.io/bk_index/chapters/5.gitbook博客搭建.html
id_map.set("5.gitbook博客搭建.html", "heuxaqknc");


require(["gitbook", "jQuery"], function (gitbook, $) {
  function resetViewCount() {
    var bookHeader = $('.book-header')
    var lastChild = bookHeader.children().last()

    var res  = decodeURI(location.href).split('/')
    var get_id = id_map.get(res[res.length-1].split('?h')[0])

    var t = Date.now();
    var src= 'https://www.cutercounter.com/hits.php?id='+get_id+'&nd=1&style='+counter_style+'?t='+t;

    var renderWrapper = $('<div class="page-view-wrapper dropdown pull-left">\
        <span class="btn toggle-dropdown">'+ iconSVg + '</span>\
        <img id="count_id" src="'+src+'" border="0" alt="免费计数器" height=32/>\
      </div>')

    if(lastChild.length){
      renderWrapper.insertBefore(lastChild)
    }else{
      bookHeader.append(renderWrapper)
    }
  }

  gitbook.events.bind("page.change", resetViewCount)
}
);
