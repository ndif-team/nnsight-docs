:html_theme.sidebar_secondary.remove:

.. role:: raw-html(raw)
   :format: html

.. raw:: html

   <script>
   document.addEventListener('DOMContentLoaded', (event) => {
      document.querySelectorAll('h5.card-title').forEach(el => {
      el.style.margin = '0';
      });
   });
   </script>

   <style>
      .toctree-wrapper {
         display: none !important;
      }
      h5 {
         margin-top: 0 !important;
      }
   </style>


Tutorials
=========

.. grid:: 1 1 1 1 
   :class-container: tutorial-card-section
   :gutter: 3

   .. grid-item-card:: 
      :link: walkthroughs.html
      :class-card: surface
      :class-body: surface

      .. raw:: html

         <div class="d-flex align-items-center">
            <div class="d-flex justify-content-center" style="min-width: 50px; margin-right: 15px; height: 100%;">
               <i class="fa-solid fa-book fa-2x"></i>
            </div> 
            <div>
               <h5 class="card-title">Main Tutorials</h5>
               <p class="card-text">Learn interpretability through step-by-step tutorials</p>
            </div>
         </div>


   .. grid-item-card:: 
      :link: applied_tutorials.html
      :class-card: surface
      :class-body: surface

      .. raw:: html

         <div class="d-flex align-items-center">
            <div class="d-flex justify-content-center" style="min-width: 50px; margin-right: 15px; height: 100%;">
               <i class="fa-solid fa-flask fa-2x"></i>
            </div> 
            <div>
               <h5 class="card-title">Mini Papers</h5>
               <p class="card-text">Get hands-on experience with recent papers in interpretability</p>
            </div>
         </div>

Report Issues
-------------

NNsight and NDIF are open-source and you can report issues, read, and clone the full source at https://github.com/ndif-team/nnsight. 
Also check out https://discuss.ndif.us/ to ask questions about our tutorials, share your projects in NNsight, or request new tutorials.


.. toctree::
   :maxdepth: 1

   Main Tutorials <walkthroughs>
   Mini Papers <applied_tutorials>