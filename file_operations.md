# Powershell File Operations

Now that we know how to move in the file system, let's check how to manipulate files and folders. In this challenge, you will discover and use the commands `Get-Content`, `echo`, `New-Item`, `Move-Item`, `Copy-Item`, and `Remove-Item`.

- Create a file named story1.txt

  | new-item story1.txt |
  | ------------------- |

  

- Type `echo "Hello World" > story1.txt`

- Print the content of the file

  | get-content story1.txt |
  | ---------------------- |

  ![image-20230623084831243](C:\Githubciscopackettraceractivity\not finished\image1-20230623084831243.png)

  

- Create a folder named `story`

  | new-item story |
  | -------------- |
  | mkdir story    |

  

- Move `story1.txt` inside `story`2

  | move-item story1.txt story2 |
  | --------------------------- |
  |                             |

  

- Copy `story1.txt` as `story2.txt` 

  | copy-item c:/users/mitu/story1.txt c:/users/mitu/story2.txt |
  | ----------------------------------------------------------- |

  

- Print both files

  | get-content story1.txt,story2.txtme |
  | ----------------------------------- |

  

- Rename `story2.txt` as `me.txt`

  | rename-item story2.txt me.txt |
  | ----------------------------- |

  

- Append `me.txt` and add "I am a junior at Becode"

  | add-content me.txt "I am junior at Becode" |
  | ------------------------------------------ |

  

- Remove the folder story with its content

  | remove-item story |
  | ----------------- |

  
