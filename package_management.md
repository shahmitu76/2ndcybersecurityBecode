# Powershell Package Management

It's time to start installing softwares and keep them updated. We will see how to use Chocolatey and how to use Windows Updates.

* Instructions

- ## Get Windows updates
    
    - ### Install the `PSWindowsUpdate` module
    
      Open PowerShell as an administrator: Press `Win + X` and select "Windows PowerShell (Admin)".
    
      Check if the PSGallery repository is trusted: Run the following command to check the value of the `PSGallery` repository's Trusted parameter:
    
      - ```
        
        Get-PSRepository
        ```
    
      If the `Trusted` parameter is set to `False` for the `PSGallery` repository, you need to change it to `True`. To do that, run the following command:
    
      ```
      
      Set-PSRepository -Name PSGallery -InstallationPolicy Trusted
      ```
    
      1. Install the PSWindowsUpdate module: Run the following command to install the module from the PSGallery repository:
    
         ```
         
         Install-Module -Name PSWindowsUpdate
         ```
    
      2. Confirm the installation: You may be prompted to install the NuGet provider or update the package provider. If prompted, enter "Y" and press Enter to proceed.
    
      3. Import the PSWindowsUpdate module: After the installation is complete, import the module by running the following command:
    
         ```
         powershellCopy code
         Import-Module -Name PSWindowsUpdate
         ```
    
      That's it! The PSWindowsUpdate module should now be installed and ready to use in your PowerShell session
    
    - Type `Get-WindowsUpdate` to check for updates-Done
    - Type `Install-WindowsUpdate` to install updates-Done
    
- # Manage Packages
    
    - ### Install `Chocolatey`
    
    To install Chocolatey, a package manager for Windows, you can follow these steps:
    
    1. Open PowerShell as an administrator: Press `Win + X` and select "Windows PowerShell (Admin)".
    
    2. Enable script execution: By default, PowerShell restricts running scripts. To change this setting, run the following command:
    
       ```
       powershellCopy code
       Set-ExecutionPolicy Bypass -Scope Process -Force
       ```
    
    - Install Chocolatey: Run the following command to download and install Chocolatey:
    
      ```
      powershellCopy code
      iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
      ```
    
      This command will download the Chocolatey installation script and execute it.
    - Verify the installation: After the installation completes, close and reopen PowerShell. Then, run the following command to verify that Chocolatey is installed:
    
      ```
      powershellCopy code
      choco
      ```
    
    - 
    - It will show the version of chocolatey.
    
    
    
    ![image-20230623135313045](C:\Users\nimes\AppData\Roaming\Typora\typora-user-images\image-20230623135313045.png)
    
    
    
    
    
    - 
    - # Install `VLC` from `Chocolatey`
    
    
    
    
    
    
    
    - Upgrade `VLC` to the latest version (it should already be but it's your first use)
    
    | choco upgrade vlc |
    | ----------------- |
    
    
    
    - Remove the `VLC` package using `Chocolatey`
    
      | choco uninstall vlc |
      | ------------------- |
    
      
    
    
    
    ![image-20230623140445242](C:\Users\nimes\AppData\Roaming\Typora\typora-user-images\image-20230623140445242.png)
    
    - Could you use `Chocolatey` on already installed software? How? Yes, mentioned above
    
- ## Manage Windows Features
    
    - ### Get installed windows features with the command `Get-WindowsFeature`
    
    - Its not available for Windows10.(client)
    
    - so,I used this command:
    
      | Get-WindowsOptionalFeature -Online |
      | ---------------------------------- |
    
      Please note, you have always to be on administrator screen.
    
    - ### Install a new feature such as hyper-v with `Install-WindowsFeature`
    
    - for this: I had to install first parent feature of Hyper-v and that too online.
    
    - | Enable-WindowsOptionalFeature -FeatureName Microsoft-Hyper-V-All -Online |
      | :----------------------------------------------------------: |
    
      After Enabling this, my windows automatically restarted.
    
      Once the required parent features are enabled, you enabled  the Hyper-V feature using the command:
    
      ```
      
      Enable-WindowsOptionalFeature -FeatureName Microsoft-Hyper-V -Online
      ```
    
- Done!!!
