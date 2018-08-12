<html>
<head>
  <style type="text/css">
    body {
      background-color: #36393f;
      color: #DCDDDE;
      text-align: center;
    }
    h3 {
        color: #EEA34A
    }
    #table {
        margin: 0 auto;
    }
    .title {
        color: #EEA34A;
    }
    .input {
      -webkit-box-shadow: 0px 1px rgba(255, 255, 255, 0.5);
      -moz-box-shadow: 0px 1px rgba(255, 255, 255, 0.5);
      -moz-box-shadow: 0px 1px rgba(255, 255, 255, 0.5);
      box-shadow: 0px 1px rgba(255, 255, 255, 0.5);
      -webkit-border-radius: 3px;
      -moz-border-radius: 3px;
      border-radius: 3px;
      width: 300px;
    }
    .input:focus {
      border:solid 1px #EEA34A;
    }
    .input:focus::-webkit-input-placeholder { 
      color:transparent; 
    }
    input:focus:-moz-placeholder { 
      color:transparent; 
    }
    input:focus::-moz-placeholder { 
      color:transparent; 
    }
    footer {
      position: fixed;
      bottom: 0px;
      width: 1350px;
      width: 100%;
      margin-bottom: 10px;
    }
    footer #license {
      color: white;
      font-size: 10px;
      margin: 0 auto;
    }
    
    a:link { 
      color: white; 
    }
    a:visited { 
      color: white; 
    }
    a:hover {
      color: #ff0000; 
    }
    a:active { 
      color: #ff8000; 
    }
  </style>

</head>
<body>
    <h3>設定</h3>
  <p>{{statusMessage}}</p>
  <form action="/setting" method="post">
    <div id="table">
    <table align="center">
      <tr>
        <td colspan="2">WorldOfWarships.exeが配置されているディレクトリをフルパスで入力</td>
      </tr>
      <tr>
        <td class="title">WoWs Path:</td>
        <td><input class="input" name="wowsPath" type="text" value="C:\Games\World_of_Warships" /></td>
      </tr>
      <tr>
        <td colspan="2"><a href="https://developers.wargaming.net/applications/">Developers Room</a>
            で作成したアプリケーションIDを入力</td>

      </tr>
      <tr>
        <td class="title">APP Key:</td>
        <td><input class="input" name="appId" type="text" placeholder="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"/></td>
      </tr>
      <tr>
        <td colspan="2">ゲーム内の名前</td>
      </tr>
      <tr>
        <td class="title">IGN:</td>
        <td><input class="input" name="ign" type="text" placeholder="Akane_Kotonoha" /></td>
      </tr>
      <tr>
        <td colspan="2">プレイしているサーバーを選択</td>
      </tr>
      <tr>
        <td class="title">Region:</td>
        <td><select name="region">
          <option value="asia">ASIA</option>
          <option value="asia">NA</option>
          <option value="asia">EU</option>
          <option value="asia">RU</option>
        </select></td>
      </tr>

    </table>
    </div>
    <br>
    <input value="登録" type="submit" />
  </form>
  <footer>
        <p id="license">The MIT License (MIT) Copyright (c) 2018 4KaNE
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            Please send request and bug report to 
            <a href="https://github.com/4KaNE/wows-stats-python">GitHub</a>
            or <a href="https://twitter.com/4KaNE_NiER">Twitter</a>.</p>
    </footer>
</body>
</html>
