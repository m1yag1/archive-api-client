==================
Archive API Client
==================

A Python wrapper around the Archive web api.


Quick start
-----------

Instantiate the ``ArchiveClient``:

.. code-block:: python

    client = ArchiveClient()


Get a collection:

.. code-block:: python

    collection = client.get_collection("7fccc9cf-9b71-44f6-800b-f9457fd64335")

You now have access to lots of information about the collection.

.. code-block:: bash

    collection.title
    >> "Chemistry 2e"
    collection.version
    >> "9.18"

If you need to access a subcollection or module you can explore ``collection.table_of_contents``

.. code-block:: bash

    toc = collection.table_of_contents
    for item in toc.contents
        print(item)
    >><Module [Preface]>
    >><SubCollection [Essential Ideas]>
    >><SubCollection [Atoms, Molecules, and Ions]>
    >><SubCollection [Composition of Substances and Solutions]>

You can grab a module from the contents and get other information:

.. code-block:: bash

    module = toc.contents[0]
    print(module.title)
    >>"Preface"
    print(module.html_title)
    >>"<span class="os-text">Preface</span>"

If you want to print the json or the html version you can do that too

.. code-block:: bash

    module = toc.contents[0]
    print(module.title)
    >>"Preface"
    module_html = module.get_html()
    print(module_html)
    >><html xmlns="http://www.w3.org/1999/xhtml"><head><meta name="robots" content="noindex"/></head><body><div data-type="page" id="138634ed-6ed0-4edb-b13d-b78d388028b0" class="preface" ...




