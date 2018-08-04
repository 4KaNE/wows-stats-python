<html>
<head>
  <script type="text/javascript">
    function ChangeTab(tabname) {
    document.getElementById('tab1').style.display = 'none';
    document.getElementById('tab2').style.display = 'none';
    document.getElementById('tab3').style.display = 'none';
    document.getElementById('tab4').style.display = 'none';

    document.getElementById(tabname).style.display = 'block';
  }
  </script>
  <link rel="stylesheet" href="/static/css/style.css" type="text/css" />
  <link rel="icon" href="/static/images/Favicon.ico" />
</head>
<body>

<div>
  <p>現在戦闘中ではありません</p>
</div>

<div class="tabbox">

  <p class="tabs">
    <a href="#tab1" class="tab1" onclick="ChangeTab('tab1'); return false;">戦闘</a>
    <a href="#tab2" class="tab2" onclick="ChangeTab('tab2'); return false;">個人戦績</a>
    <a href="#tab3" class="tab3" onclick="ChangeTab('tab3'); return false;">艦別戦績</a>
    <a href="#tab4" class="tab4" onclick="ChangeTab('tab3'); return false;">設定</a>
  </p>
  <div id="tab1" class="tab">
    <h1>戦闘中の敵・味方プレイヤーの戦績を表示します。</h1>
    <div id="playerNo">
      <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
        <li>6</li>
      </ul>
    </div>
  </div>

  <div id="tab2" class="tab">
    <h2>Akane_Kotonoha</h2>
    <h1>自分の総合戦績を表示します。ほかのプレイヤーの戦績の検索、閲覧も可能です。</h1>
　</div>

  <div id="tab3" class="tab">
    <h1>艦別の戦績を表示します。自由に追加、削除できるリスト形式で表示する予定です。</h1>
  </div>

  <div id="tab4" class="tab">
    <h1>設定</h1>
  </div>


</div>

<script type="text/javascript">
  ChangeTab('tab1');
</script>



</body>
</html>
