const { app, BrowserWindow } = require('electron')
const { exec } = require('child_process')

function createWindow () {
  const win = new BrowserWindow({
    width: 1300,
    height: 850,
    backgroundColor: "#0f172a"
  })

  win.loadURL("http://127.0.0.1:8000")
}

app.whenReady().then(() => {
  exec("bash start.sh")
  setTimeout(createWindow, 4000)
})
