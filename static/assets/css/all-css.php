<?php
// First of all send css header
header("Content-type: text/css");

// Array of css files
$css = array(
'bootstrap.min.css',
'font-awesome.css',
'magnific-popup.css',
'owl.carousel.css',
'jquery.mCustomScrollbar.css',
'styles/style.css',
'styles/skin-lblue.css',
'custom.css',
'map-icons.css',
'styles/restaurant.css',
'styles/real-estate.css',
);

// Prevent a notice
$css_content = '';

// Loop the css Array
foreach ($css as $css_file) {
    $css_content .= file_get_contents($css_file);
}

echo $css_content;