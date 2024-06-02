// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      2024-05-31
// @description  try to take over the world!
// @author       You
// @match        https://pgexercises.com/questions/aggregates/classify.html
// @icon         https://www.google.com/s2/favicons?sz=64&domain=pgexercises.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    document.querySelector('#codewrapper > form > div').style.height = "600px";
    document.querySelector('#youranswerdiv').style.height = "600px";
    document.querySelector('#splittercontainer').style.height = "1000px";
})();
