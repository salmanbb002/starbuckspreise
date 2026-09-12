// Native details remain usable without JavaScript. Start the contents list
// collapsed on small screens so readers reach the article immediately.
const contents = document.querySelector('.article-toc');
if (contents) {
  const compactLayout = window.matchMedia('(max-width: 900px)');
  const setContentsLayout = () => { contents.open = !compactLayout.matches; };
  setContentsLayout();
  compactLayout.addEventListener('change', setContentsLayout);
}
