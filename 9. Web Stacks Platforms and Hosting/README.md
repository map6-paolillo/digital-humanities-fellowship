# Day 9: The Web Stack, Platforms, & Hosting

## A Good General Reference  
[Understanding the digital world : what you need to know about computers, the Internet, privacy, and security / Brian W. Kernighan](https://newcatalog.library.cornell.edu/catalog/9771623)

## Hosting Your Web Site: Static vs. Dynamic  

The components of a basic website are HTML, CSS, & JavaScript (JS). All of these languages operate on the *client side.* Languages  A static site is one that uses just these three languages, and is rendered the same each time. A more complicated web site, called a dynamic web site, relies on a content management system (see below), and renders each web page as it is called. 

### Static Web Sites 

If you need a static web site that is secure and easy to maintain, the software Jekyll and the host [GitHub Pages](https://pages.github.com/) might be a good option. There's a little bit of set up to learn, but once you're set up, your pages are straight-forward to write and maintain. 

*Programming Historian* has [a good tutorial on setting up a Jekyll site hosted by GitHub Pages](https://programminghistorian.org/en/lessons/building-static-sites-with-jekyll-github-pages) (by Amanda Visconti).  

GitHub Pages is a no-fee host. It's free to use. However, it's good to know that GitHub is a commercial company owned by Microsoft, and can change its terms of service at any time. The good news is that Jekyll makes it easy to export and transport your site to a different host if you want to, for any reason. 

Examples of web sites built with Jekyll (some hosted on GitHub Pages):  
* [UN World Statistics Day](https://worldstatisticsday.org/)  
* [Leaflet for R](https://rstudio.github.io/leaflet/)  
* [Collections as Data: Part to Whole](https://collectionsasdata.github.io/part2whole/)  

Anytime you see the domain github.io, that page is built with Jekyll and hosted on GitHub Pages.

### Dynamic Web Sites  

If your web site needs a content management system, or a relational database, or other *client-side* programming, you will need a place to host it. You have two basic options:

1. Lease your own space. Have full access to the back end. Install whatever you want there.  
  * In most cases, I recommend [Reclaim Hosting](https://reclaimhosting.com/shared-hosting/). It's designed for scholars, has fantastic technical support, and makes it really easy to install your own instance(s) of Wordpress, Omeka, Scalar, mySQL, and many more platforms. You can also start from scratch and host any HTML, CSS, and/or JS that you write (or borrow/adapt) here. Security and back ups are covered for you. You can register any domain name you like (or move an existing one over). Cost for a personal plan is $30/year. 
  * In a few cases you might want to install something that Reclaim doesn't support easily. One example is PostGIS, a spatial relational database software. In that case you would need to get some developer cloud space at a host like [Digital Ocean](https://www.digitalocean.com/).  
  
2. Use some of the the CoLab's space.  
  * The CoLab has an organizational account (100 GB) through Reclaim. If you're not ready to buy your own space, or you just want a temporary space to experiement, you can use some of it for your own installation of Omeka, Scalar, Wordpress, or another software package. The domain You won't have your own access to the backend of the server itself (so you can't write your code from scratch), but you *can* access the back end of whatever software installation you have are using, and if/when you're ready to migrate it over to your own Reclaim (or other) space, you can. The domain name will be cornellcolab.net. 
  * CoLab space is also a good solution if you're teaching a class and your students need space for their projects. (See undergrad examples below.) You can talk to Eliza anytime about getting space for student assignments.  
  
### When You Just Want to Share Your Code  

Let's say you have data or software that you've written and want to make available to others. The standard place to do that is GitHub. If you want, you can also produce a static web site in GitHub Pages that links to your code repository.  

Here are examples of digital projects hosted on GitHub:  
* La Gaceta de la Habana  
* Intertext  

Here is an example of a GitHub Pages front page for a series of code repositories hosted on GitHub:  
* [Data and Visualization Workshops at NCSU](https://ncsu-libraries.github.io/data-viz-workshops/)  



## Web Exhibits

### Omeka
[Omeka](https://omeka.org/classic/) allows you to manage collections of archival objects (including photos, audio, and video) and their metadata, and to create exhibitions from them.  

* Free and open-source software platform developed at George Mason University for academic, museum, and library users.  
* Omeka software is free, but Omeka does not provide hosting for free. You can host your own installation, or use CornellColab.net to host an installation.  
* (Alternatively, you can pay Omeka.net to host an installation for you, but the number of plug-ins you can use will be limited, and it's relatively expensive compared to what you get from a service like Reclaim.)
* Has a GUI. You can use CSS to extend functionality, or customize the visual style. 

Examples
* [Showcase of Omeka Projects](https://omeka.org/classic/showcase/)

Examples by Cornell undergrads
* [Rhetorical Cartography of Early Texas](http://cornellcolab.net/EarlyAmericanMaps/exhibits/show/mappingtexas)  
* [Saints and Gentiles: Utah's Unconventional Path to Statehood](http://cornellcolab.net/EarlyAmericanMaps/exhibits/show/utah-statehood/introduction)  

Some Good References for Using Omeka
[Up and Running with Omeka.net](https://programminghistorian.org/en/lessons/up-and-running-with-omeka) by Miriam Posner, *The Programming Historian*  
[Creating an Omeka Exhibit](https://programminghistorian.org/en/lessons/creating-an-omeka-exhibit) by Miriam Posner & Megan R. Brett, *The Programming Historian*  

### Wax  
[Wax](https://minicomp.github.io/wax/about/) is a system for creating web exhibits released just a week ago by Columbia University Library.  

* Unlike Omeka, it is built with static sheets, which means it's lighter weight, easier to preserve, and easier to migrate.  
* Limited (or no?) GUI, so you need to use the command line (Terminal) to interact with the objects and the exhibit.  
* But think of all the things you can learn!  

[Examples of Exhibits Built with Wax](https://minicomp.github.io/wiki/wax/examples/)  
See especially [Style Revolution](https://stylerevolution.github.io/)

[Instructions for Using Wax](https://minicomp.github.io/wiki/wax/)

## Web Publishing

### Scalar
* [Performing Archive: Curtis + "the vanishing race"](http://scalar.usc.edu/works/performingarchive/index)
* [Mapping Jewish LA](http://www.mappingjewishla.org/)

[Scalar User Guide](http://scalar.usc.edu/works/guide2/index)

### Wordpress
* [Parthian Sources Online](http://parthiansources.com/)

Also see: [Wordpress.com Features](https://en.wordpress.com/features/)

## Maps

### Carto

* Proprietary, commercial platform
* Can embed on dynamic sites
* (Embed on static sites? Not sure! TBD soon.)  
* Can extend functionality with Leaflet.js, CSS, SQL 

Examples  
* [Mapping Islamophobia](http://mappingislamophobia.org/)
* [Communal Currents](https://communalcurrents.org/)

Also see: [Carto Builder overview](https://carto.com/builder/)

### Neatline
[Neatline](http://neatline.org) is a sophisticated plugin for Omeka that allows mapping. It was developed at the University of Virginia, and, like Omeka, is designed for academic users. Check out some of the example projects made with Neatline, and compare with Carto. One difference between the two is that Omeka allows much more freeform annotation, and various ways of embedding collections of objects within the map. Neatline also offers timeline tools.

In order to use Neatline, you must host your own installation of Omeka (or use one installed on the CoLab space). 

* [The Hereford Map](http://historiacartarum.org/john-mandeville-and-the-hereford-map-2/what-are-you/) by Cornell Ph.D. candidate John Wyatt Greenlee  
* [Brooklyn Anthems Atlas](http://cornellcolab.net/BrooklynAnthemsAtlas/neatline/fullscreen/brooklyn-anthems-atlas) by Cornell undergrad Avi Simon  
* [More Neatline Examples](https://neatline.org/demos/)

### Mapbox
[Mapbox](http://Mapbox.com)  

### Javascript Languages
LeafletJS
D3JS







