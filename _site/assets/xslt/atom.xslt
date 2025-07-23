<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:atom="http://www.w3.org/2005/Atom">
<xsl:output method="html" encoding="utf-8" />
<xsl:template match="/atom:feed">
	<xsl:text disable-output-escaping="yes">&lt;!DOCTYPE html &gt;</xsl:text>
	<html>
	<head>
		<xsl:text disable-output-escaping="yes"><![CDATA[
		<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Atom Feed (Styled)</title>

    <link rel="stylesheet" type="text/css" href="http://localhost:4000/assets/css/styles_feeling_responsive.css">

  

	<script src="http://localhost:4000/assets/js/modernizr.min.js"></script>

	<script src="https://ajax.googleapis.com/ajax/libs/webfont/1.5.18/webfont.js"></script>
	<script>
		WebFont.load({
			google: {
				families: [ 'Lato:400,700,400italic:latin', 'Volkhov::latin' ]
			}
		});
	</script>

	<noscript>
		<link href='http://fonts.googleapis.com/css?family=Lato:400,700,400italic%7CVolkhov' rel='stylesheet' type='text/css'>
	</noscript>


	<!-- Search Engine Optimization -->
	<meta name="description" content="Design. Develop. Deliver">
	
	
	
	
	
	<link rel="canonical" href="http://localhost:4000/assets/xslt/atom.xslt">


	<!-- Facebook Open Graph -->
	<meta property="og:title" content="Atom Feed (Styled)">
	<meta property="og:description" content="Design. Develop. Deliver">
	<meta property="og:url" content="http://localhost:4000/assets/xslt/atom.xslt">
	<meta property="og:locale" content="en_EN">
	<meta property="og:type" content="website">
	<meta property="og:site_name" content="Delta3Consulting">
	
	


	
	<!-- Twitter -->
	<meta name="twitter:card" content="summary">
	<meta name="twitter:site" content="dustinson">
	<meta name="twitter:creator" content="dustinson">
	<meta name="twitter:title" content="Atom Feed (Styled)">
	<meta name="twitter:description" content="Design. Develop. Deliver">
	
	

	<link type="text/plain" rel="author" href="http://localhost:4000/humans.txt">

	

	

	<link rel="icon" sizes="32x32" href="http://localhost:4000/assets/img/favicon.ico">

	<link rel="icon" sizes="192x192" href="http://localhost:4000/assets/img/favicon.ico">

	<link rel="apple-touch-icon-precomposed" sizes="180x180" href="http://localhost:4000/assets/img/favicon.ico">

	<link rel="apple-touch-icon-precomposed" sizes="152x152" href="http://localhost:4000/assets/img/favicon.ico">

	<link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://localhost:4000/assets/img/favicon.ico">

	<link rel="apple-touch-icon-precomposed" sizes="120x120" href="http://localhost:4000/assets/img/favicon.ico">

	<link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://localhost:4000/assets/img/favicon.ico">

	
	<link rel="apple-touch-icon-precomposed" sizes="76x76" href="http://localhost:4000/assets/img/favicon.ico">

	<link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://localhost:4000/assets/img/favicon.ico">

	<link rel="apple-touch-icon-precomposed" href="http://localhost:4000/assets/img/favicon.ico">	

	<meta name="msapplication-TileImage" content="http://localhost:4000/assets/img/favicon.ico">

	<meta name="msapplication-TileColor" content="#fabb00">


	

	


		]]></xsl:text>
	</head>
	<body id="top-of-page">
		<xsl:text disable-output-escaping="yes"><![CDATA[
		
<div id="navigation" class="sticky">
    <nav class="top-bar" role="navigation" data-topbar data-options="scrolltop: false">
        <ul class="title-area">
            <li class="name">
                <h1 class="hide-for-large-up"><a href="http://localhost:4000/"> Delta3Consulting</a></h1>
            </li>
            <!-- Remove the class "menu-icon" to get rid of menu icon. Take out "Menu" to just have icon alone -->
            <li class="toggle-topbar toggle-topbar-click menu-icon"><a><span>Nav</span></a></li>
        </ul>
        <section class="top-bar-section">
            
            <ul class="left">
                

                

                
                

                
                
                <li
                        ><a 
                                             href="http://localhost:4000/" >
                
                <img src="http://localhost:4000/images/Delta3Consulting.png" alt="d3" width="420PX"/>
                
                </a></li>
                <li class="divider"></li>

                
                
                
                

                

                
                

                
                
                <li
                        ><a 
                                             href="http://localhost:4000/events/" >
                
                Events</a></li>
                <li class="divider"></li>

                
                
                
                

                

                
                

                
                
                <li
                        ><a 
                                             href="http://localhost:4000/blog/" >
                
                Blog</a></li>
                <li class="divider"></li>

                
                
                
                

                

                
                

                
                
                <li
                        ><a 
                                             href="https://www.youtube.com/playlist?list=PLu5A5CyoWE0aYG6Fosb113fD_VQv3-VRn"  target="_blank">
                
                Videos</a></li>
                <li class="divider"></li>

                
                
                
                
                
            </ul>


            
            <ul class="right">
                

                


                
                
                

                


                
                
                

                


                
                
                

                


                
                
                
                
            </ul>

        </section>
    </nav>
</div><!-- /#navigation -->

		

<div id="masthead-no-image-header">
    <div class="row">
<!--        <div class="small-12 columns" style="position:absolute; width:10%; height:10%">-->
<!--            <a id="logo" href="http://localhost:4000/" title="Delta3Consulting – Design, Develop, Deliver">-->
<!--                <img src="http://localhost:4000/assets/img/D3Logo.png"-->
<!--                     alt="Delta3Consulting – Design, Develop, Deliver">-->
<!--            </a>-->
<!--        </div>&lt;!&ndash; /.small-12.columns &ndash;&gt;-->
    </div><!-- /.row -->
</div><!-- /#masthead -->





		


<div class="alert-box warning text-center"><p>This <a href="https://en.wikipedia.org/wiki/RSS" target="_blank">Atom feed</a> is meant to be used by <a href="https://en.wikipedia.org/wiki/Template:Aggregators" target="_blank">RSS reader applications and websites</a>.</p>
</div>



		]]></xsl:text>
		<header class="t30 row">
	<p class="subheadline"><xsl:value-of select="atom:subtitle" disable-output-escaping="yes" /></p>
	<h1>
		<xsl:element name="a">
			<xsl:attribute name="href">
				<xsl:value-of select="atom:id" />
			</xsl:attribute>
			<xsl:value-of select="atom:title" />
		</xsl:element>
	</h1>
</header>
<ul class="accordion row" data-accordion="">
	<xsl:for-each select="atom:entry">
		<li class="accordion-navigation">
			<xsl:variable name="slug-id">
				<xsl:call-template name="slugify">
					<xsl:with-param name="text" select="atom:id" />
				</xsl:call-template>
			</xsl:variable>
			<xsl:element name="a">
				<xsl:attribute name="href"><xsl:value-of select="concat('#', $slug-id)"/></xsl:attribute>
				<xsl:value-of select="atom:title"/>
				<br/>
				<small><xsl:value-of select="atom:updated"/></small>
			</xsl:element>
			<xsl:element name="div">
				<xsl:attribute name="id"><xsl:value-of select="$slug-id"/></xsl:attribute>
				<xsl:attribute name="class">content</xsl:attribute>
				<h1>
					<xsl:element name="a">
						<xsl:attribute name="href"><xsl:value-of select="atom:id"/></xsl:attribute>
						<xsl:value-of select="atom:title"/>
					</xsl:element>
				</h1>
				<xsl:value-of select="atom:content" disable-output-escaping="yes" />
			</xsl:element>
		</li>
	</xsl:for-each>
</ul>

		<xsl:text disable-output-escaping="yes"><![CDATA[
		<div id="up-to-top" class="row" xmlns="http://www.w3.org/1999/html">
      <div class="small-12 columns" style="text-align: right;">
        <a class="iconfont" href="#top-of-page">&#xf108;</a>
      </div><!-- /.small-12.columns -->
    </div><!-- /.row -->


    <footer id="footer-content" class="bg-grau">
<!--      <div id="footer">-->
<!--        <div class="row">-->
<!--          <div class="medium-6 large-5 columns">-->
<!--            <h5 class="shadow-black">About This Site</h5>-->

<!--            <p class="shadow-black">-->
<!--              Design. Develop. Deliver-->
<!--              <a href="http://localhost:4000/info/">More ›</a>-->
<!--            </p>-->
<!--          </div>&lt;!&ndash; /.large-6.columns &ndash;&gt;-->


<!--          <div class="small-6 medium-3 large-3 large-offset-1 columns">-->
<!--            -->
<!--              -->
<!--                <h5 class="shadow-black">Services</h5>-->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->

<!--              <ul class="no-bullet shadow-black">-->
<!--              -->
<!--                -->
<!--                  <li >-->
<!--                    <a href="http://localhost:4000"  title=""></a>-->
<!--                  </li>-->
<!--              -->
<!--                -->
<!--                  <li >-->
<!--                    <a href="http://localhost:4000/contact/"  title="Contact">Contact</a>-->
<!--                  </li>-->
<!--              -->
<!--                -->
<!--                  <li >-->
<!--                    <a href="http://localhost:4000/feed.xml"  title="Subscribe to RSS Feed">RSS</a>-->
<!--                  </li>-->
<!--              -->
<!--                -->
<!--                  <li >-->
<!--                    <a href="http://localhost:4000/atom.xml"  title="Subscribe to Atom Feed">Atom</a>-->
<!--                  </li>-->
<!--              -->
<!--                -->
<!--                  <li >-->
<!--                    <a href="http://localhost:4000/sitemap.xml"  title="Sitemap for Google Webmaster Tools">sitemap.xml</a>-->
<!--                  </li>-->
<!--              -->
<!--              </ul>-->
<!--          </div>&lt;!&ndash; /.large-4.columns &ndash;&gt;-->


<!--          <div class="small-6 medium-3 large-3 columns">-->
<!--            -->
<!--              -->
<!--                <h5 class="shadow-black">Organizations we've worked with</h5>-->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->
<!--              -->
<!--            -->

<!--            <ul class="no-bullet shadow-black">-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title=""></a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">Principal Financial Group</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">Ford Motor Company</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">TDAmeritrade</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">Industrial Logic</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">Lean TECHniques</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">JohnDeere</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">Berkley Technology Services</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">Pioneer HyBrid</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">Summit Healthcare</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">Iowa League Of Cities</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">Agile Alliance</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">VisionT</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">Rockline Enterprises</a>-->
<!--                </li>-->
<!--            -->
<!--              -->
<!--                <li >-->
<!--                  <a href="http://localhost:4000"  title="">BirdDogJobs</a>-->
<!--                </li>-->
<!--            -->
<!--            </ul>-->
<!--          </div>&lt;!&ndash; /.large-3.columns &ndash;&gt;-->
<!--        </div>&lt;!&ndash; /.row &ndash;&gt;-->

<!--      </div>&lt;!&ndash; /#footer &ndash;&gt;-->


      <div id="subfooter">
        <nav class="row">
          <section id="subfooter-left" class="small-12 medium-6 columns credits">
            
          </section>

          <section id="subfooter-right" class="small-12 medium-6 columns">
            <ul class="inline-list social-icons">
            
              <li><a href="http://twitter.com/dustinson" target="_blank" class="icon-twitter" title="@Dustinson on Twitter"></a></li>
            
              <li><a href="https://www.youtube.com/playlist?list=PLu5A5CyoWE0aYG6Fosb113fD_VQv3-VRn" target="_blank" class="icon-youtube" title="Videos"></a></li>
            
              <li><a href="https://www.linkedin.com/in/dustinthostenson/" target="_blank" class="icon-linkedin" title="Let's Connect"></a></li>
            
            </ul>
          </section>
        </nav>
      </div><!-- /#subfooter -->
    </footer>

		


<script src="http://localhost:4000/assets/js/javascript.min.js"></script>












		]]></xsl:text>
	</body>
	</html>
</xsl:template>
<xsl:template name="slugify">
	<xsl:param name="text" select="''" />
	<xsl:variable name="dodgyChars" select="' ,.#_-!?*:;=+|&amp;/\\'" />
	<xsl:variable name="replacementChar" select="'-----------------'" />
	<xsl:variable name="lowercase" select="'abcdefghijklmnopqrstuvwxyz'" />
	<xsl:variable name="uppercase" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZ'" />
	<xsl:variable name="lowercased"><xsl:value-of select="translate( $text, $uppercase, $lowercase )" /></xsl:variable>
	<xsl:variable name="escaped"><xsl:value-of select="translate( $lowercased, $dodgyChars, $replacementChar )" /></xsl:variable>
	<xsl:value-of select="$escaped" />
</xsl:template>
</xsl:stylesheet>
