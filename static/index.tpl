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
  <!-- 戦闘タブ -->
  <div id="tab1" class="tab">
    <table id="description_table">
      <tr>
        <td>味方</td>
      </tr>
    </table>
    <table>
      <thead>
        <tr>
          <th id="clan_th">CLAN</th>
          <th id="ign_th">IGN</th>
          <th id="tier_th">T</th>
          <th id="shipclass_th">艦種</th>
          <th id="shipname_th">艦名</th>
          <th id="combatpower_th">戦闘力</th>
          <th id="combatpower_th">戦闘力2</th>
          <th id="damage_th">ダメージ</th>
          <th id="kd_th">K/D</th>
          <th id="winrate_th">勝率</th>
          <th id="survive_th">生存率</th>
          <th id="shootdown_th">撃墜</th>
          <th id="exp_th">経験値</th>
          <th id="battlenumber_th">戦闘数</th>
          <th id="rank_th">ランク</th>
          <th id="winrate_th">勝率</th>
          <th id="exp_th">経験値</th>
          <th id="battlenumber_th">戦闘数</th>
        </tr>
      </thead>
      <tbody>
        <script type="text/javascript">
          for (var i = 1; i <= 12; i++){
            document.write('<tr>')
            document.write('<td id="clan_td">CLANA</td>');
            document.write('<td id="ign_td">ABCDEFGHIJKLMNOPQR</td>');
            document.write('<td id="tier_td">10</td>');
            document.write('<td id="shipclass_td">CV</td>');
            document.write('<td id="shipname_td">Oktyabrskaya Revolutsiya</td>');
            document.write('<td id="combatpower_td">10,000,000</td>');
            document.write('<td id="combatpower_td">10,000,000</td>');
            document.write('<td id="damage_td">100,000</td>');
            document.write('<td id="kd_td">999.9</td>');
            document.write('<td id="winrate_td">100.0%</td>');
            document.write('<td id="survive_td">100%|100%</td>');
            document.write('<td id="shootdown_td">99.9</td>');
            document.write('<td id="exp_td">9,999</td>');
            document.write('<td id="battlenumber_td">99,999</td>');
            document.write('<td id="rank_td">23→23</td>');
            document.write('<td id="winrate_td">100.0%</td>');
            document.write('<td id="exp_td">9,999</td>');
            document.write('<td id="battlenumber_td">99,999</td>');
            document.write('</tr>')
          }
        </script>
      </tbody>
    </table>
    <table id="description_table">
      <tr>
        <td>敵</td>
      </tr>
    </table>
    <table>
        <thead>
          <tr>
            <th id="clan_th">CLAN</th>
            <th id="ign_th">IGN</th>
            <th id="tier_th">T</th>
            <th id="shipclass_th">艦種</th>
            <th id="shipname_th">艦名</th>
            <th id="combatpower_th">戦闘力</th>
            <th id="combatpower_th">戦闘力2</th>
            <th id="damage_th">ダメージ</th>
            <th id="kd_th">K/D</th>
            <th id="winrate_th">勝率</th>
            <th id="survive_th">生存率</th>
            <th id="shootdown_th">撃墜</th>
            <th id="exp_th">経験値</th>
            <th id="battlenumber_th">戦闘数</th>
            <th id="rank_th">ランク</th>
            <th id="winrate_th">勝率</th>
            <th id="exp_th">経験値</th>
            <th id="battlenumber_th">戦闘数</th>
          </tr>
        </thead>
        <tbody>
          <script type="text/javascript">
            for (var i = 1; i <= 12; i++){
              document.write('<tr>')
              document.write('<td id="clan_td">CLANA</td>');
              document.write('<td id="ign_td">ABCDEFGHIJKLMNOPQR</td>');
              document.write('<td id="tier_td">10</td>');
              document.write('<td id="shipclass_td">CV</td>');
              document.write('<td id="shipname_td">Oktyabrskaya Revolutsiya</td>');
              document.write('<td id="combatpower_td">10,000,000</td>');
              document.write('<td id="combatpower_td">10,000,000</td>');
              document.write('<td id="damage_td">100,000</td>');
              document.write('<td id="kd_td">999.9</td>');
              document.write('<td id="winrate_td">100.0%</td>');
              document.write('<td id="survive_td">100%|100%</td>');
              document.write('<td id="shootdown_td">99.9</td>');
              document.write('<td id="exp_td">9,999</td>');
              document.write('<td id="battlenumber_td">99,999</td>');
              document.write('<td id="rank_td">23→23</td>');
              document.write('<td id="winrate_td">100.0%</td>');
              document.write('<td id="exp_td">9,999</td>');
              document.write('<td id="battlenumber_td">99,999</td>');
              document.write('</tr>')
            }
          </script>
        </tbody>
      </table>
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

<footer>
    <p id="license">The MIT License (MIT) Copyright (c) 2018 4KaNE
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        Please send request and bug report to 
        <a href="https://github.com/4KaNE/wows-stats-python">GitHub</a>
        or <a href="https://twitter.com/4KaNE_NiER">Twitter</a>.</p>
</footer>

</html>
