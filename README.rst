Obake
=====

What is this?
-------------

Obake is a frontend of some web browser implementations out there.

::

    from obake.config import UserAgentConfiguration
    from obake.driver.macosx.webkit import Driver
    import time
    import xpath
    
    d = Driver()
    
    def entrypoint(ua):
        uac = UserAgentConfiguration()
        ua = ua.create_user_agent(uac)

        def callback(e):
            d = e.target.document
            body = d.getElementsByTagName('body').item(0)
            div = d.createElement("div")
            div.appendChild(d.createTextNode("test"))
            body.appendChild(div)
    
        ua.main_frame.addEventListener('load', callback, False)

        ua.main_frame.load('http://example.com/')
        time.sleep(10)
    
    d.init(entrypoint)
