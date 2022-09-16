# Microstates

## `sphinx_togglebutton` - Toggle content with buttons

```{image} https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif
:class: toggle
```
## Basic synthax


## Figures

## Notes

## References and bibliographies

### References

The extension `sphinxcontrib-bibtex` allows to manage the bibliography of this site.
To cite an article, add the reference in bibtex format to the `bibliography.bib` file and
refer to the citation using the bibtex keyword:

````{eval-rst}
.. tabs::

   .. tab:: Markdown (MyST)

      ..  code-block:: text


          {footcite}`michel2018`


   .. tab:: rST

      ..  code-block:: restructuredtext

          :footcite:`michel2018`
 
````

Will be rendered as {footcite}`michel2018`

### Bibliography

To insert a bibliography on the page use

````{eval-rst}
.. tabs::

   .. tab:: Markdown (MyST)

      ..  code-block:: text

         ```{footbibliography}
         ```

   .. tab:: rST

      ..  code-block:: restructuredtext

         .. footbibliography::
 
````


```{footbibliography}
```
Note that all references will also be listed in the website [](Bibliography).

## Tabbed content

Tabbed content can be added using `sphinx-tabs`:

``````restructuredtext

````{eval-rst}
.. tabs::

   .. tab:: MATLAB

      EEG microstate toolbox.

   .. tab:: PYTHON

      Pycrostates.

   .. tab:: CARTOOL

      Cartool.
````

``````



````{eval-rst}
.. tabs::

   .. tab:: MATLAB

      EEG microstate toolbox.

   .. tab:: PYTHON

      Pycrostates.

   .. tab:: CARTOOL

      Cartool.
````