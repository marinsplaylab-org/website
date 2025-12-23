// Function to load HTML files into a page
async function loadHTML(_elementId, _filePath)
{
  try
  {
    const response = await fetch(_filePath);
    if (!response.ok)
    {
      throw new Error(`Failed to load ${_filePath}: ${response.status} ${response.statusText}`);
    }

    const data = await response.text();

    const element = document.getElementById(_elementId);
    if (!element)
    {
      throw new Error(`Missing element with id="${_elementId}"`);
    }

    element.innerHTML = data;
  }
  catch (error)
  {
    console.error(error);
  }
}

function updateLayoutVars()
{
  const header = document.getElementById("header");
  const footer = document.getElementById("footer");
  const headerHeight = header ? header.offsetHeight : 0;
  const footerHeight = footer ? footer.offsetHeight : 0;

  document.documentElement.style.setProperty("--site-header-height", `${headerHeight}px`);
  document.documentElement.style.setProperty("--site-footer-height", `${footerHeight}px`);
}

// Load header/footer templates and update layout sizing once they are in place
Promise.all([
  loadHTML("header", "templates/header.html"),
  loadHTML("footer", "templates/footer.html")
]).then(updateLayoutVars);

window.addEventListener("resize", updateLayoutVars);
