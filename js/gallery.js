function initGalleryLinks()
{
  const items = document.querySelectorAll(".gallery-item[data-link]");

  items.forEach((item) =>
  {
    const link = item.dataset.link;
    if (!link)
    {
      return;
    }

    item.addEventListener("click", (event) =>
    {
      if (event.target.closest("a"))
      {
        return;
      }

      window.location.href = link;
    });

    item.addEventListener("keydown", (event) =>
    {
      if (event.key === "Enter" || event.key === " ")
      {
        if (event.target.closest("a"))
        {
          return;
        }

        event.preventDefault();
        window.location.href = link;
      }
    });
  });
}

document.addEventListener("DOMContentLoaded", initGalleryLinks);