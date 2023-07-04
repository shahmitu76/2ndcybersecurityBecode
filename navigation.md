# Powershell Navigation

Now we will learn how to move around in the filesystem with `Set-Location`, `Get-Location`, `Get-ChildItem` ...

- Print your current location on the screen-

  | Get-location or pwd |
  | ------------------- |

  

- Print the content of your current directory

  | ls or get- childitem |
  | -------------------- |

  

- Print the content of your root (`C:` _if you're running windows_, `/` _for linux_)

  | set-location c:/ ; get-childitem |
  | -------------------------------- |

  

- Go into your home folder (_C:\Users\Username or /home/Username_)

  | set-location c:/users/mitu |
  | -------------------------- |

  

- Print the content of your home

  | get-childitem; |
  | -------------- |

  

- Those commands are pretty long to type, do you know any shorter way to do it?

  | ls,cd,pwd |
  | --------- |

  
