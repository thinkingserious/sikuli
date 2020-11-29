# Desktop Automation with Sikuli and Python

## Prerequisites

This tutorial is tested on macOS version `10.15.7 (19H15)` and `11.0.1 (20B29)`.

* Install Java 8 or later
  * Verify by running `java --version`
  * If you don't have Java 8 or above, check out the [openJDK installation tutorial](https://solarianprogrammer.com/2018/09/28/installing-openjdk-macos/)
* Install Tesseract for macOS
  * `brew install tesseract`
  * Verify by running `tesseract -v`
* Download the SikuliX IDE: [download link](https://launchpad.net/sikuli/sikulix/2.0.4/+download/sikulixide-2.0.4.jar) or use `wget https://launchpad.net/sikuli/sikulix/2.0.4/+download/sikulixide-2.0.4.jar` from the command line
* Download Jython standalone jar: [download link](https://repo1.maven.org/maven2/org/python/jython-standalone/2.7.2/jython-standalone-2.7.2.jar) or use `wget https://repo1.maven.org/maven2/org/python/jython-standalone/2.7.2/jython-standalone-2.7.2.jar` from the command line
* See the SikuliX docs for a [complete list of prerequisites](http://sikulix.com/quickstart)

## Launch the Sikuli IDE

`java -jar sikulixide-2.0.4.jar`

## Run a demo from the command line

`java -jar sikulixide-2.0.4.jar -r demos/empty_trash.sikuli`

Note that you may need to adjust the images and/or source code per your environment, especially if you are working within a Windows or Linux OS or are using a different version of macOS. You can either edit the files directly or utilize the Sikuli IDE.

## References

* http://sikulix.com
* http://sikulix.com/quickstart
* https://sikulix-2014.readthedocs.io/en/latest/toc.html
* https://github.com/RaiMan/SikuliX1
