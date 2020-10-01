# Evan's Android App Store
this is really amazing this will help us in our life.


## Overview

This is a web app that crawl apps from huawei appstore and display with angularJS, also do recommendation based on users' download behavior.


## Development 

The following docs describe how you can test and develop this application further.

### Installing Dependencies

```
npm install
```

This will also run Bower, which will download the Angular files needed for the current step of the
tutorial.

### Running the Application during Development

- Run `npm start`.
- Navigate your browser to [http://localhost:8000/](http://localhost:8000/) to see the application 
- running.

## ScreenShots

![Home page](/demo/1.png?=250px)
![Search](/demo/2.png?=250px)
![Sort by scores](/demo/3.png?=250px)
![App info page](/demo/4.png?=250px)
![App info page2](/demo/5.png?=250px)

## Application Directory Layout

```
app/                     --> all the source code of the app (along with unit tests)
  bower_components/...   --> 3rd party JS/CSS libraries, including Angular and jQuery
  core/                  --> all the source code of the core module (stuff used throughout the app)
    checkmark/...        --> files for the `checkmark` filter, including JS source code, specs
    phone/...            --> files for the `core.phone` submodule, including JS source code, specs
    core.module.js       --> the core module
  img/...                --> image files
  source code, HTML templates, specs
  source code, HTML templates, specs
  app.css                --> default stylesheet
  app.module.js          --> the main app module
  index.html             --> app layout file (the main HTML template file of the app)

node_modules/...         --> development tools (fetched using `npm`)

bower.json               --> Bower specific metadata, including client-side dependencies
package.json             --> Node.js specific metadata, including development tools dependencies
```

[angular-seed]: https://github.com/angular/angular-seed
[bower]: http://bower.io/
[git-home]: https://git-scm.com
[git-setup]: https://help.github.com/articles/set-up-git/
[google-phone-gallery]: http://web.archive.org/web/20131215082038/http://www.android.com/devices/
[node-download]: https://nodejs.org/en/download/
