<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Varun Tech - Job Board</title>
  <style>
    body { margin: 0; font-family: Arial, sans-serif; background: #f5f5f5; text-align: center; }
    header, footer { background: #0066ff; color: #fff; padding: 10px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; }
    nav a { color: #fff; text-decoration: none; margin: 0 6px; font-size: 14px; }
    .btn { padding: 6px 10px; border-radius: 4px; text-decoration: none; color: #fff; font-size: 13px; }
    .btn-green { background: #00cc66; } .btn-orange { background: #ff9933; }
    .hero { padding: 30px 15px; background: #1e90ff; color: #fff; }
    .search { background: #fff; margin: -20px auto 15px; padding: 10px; max-width: 700px; border-radius: 6px; }
    .search input, .search select, .search button { padding: 8px; margin: 5px; border: 1px solid #ccc; border-radius: 4px; }
    .search button { background: #00cc66; color: #fff; border: none; }
    .jobs { display: flex; justify-content: center; flex-wrap: wrap; padding: 10px; }
    .job { background: #fff; margin: 5px; padding: 10px; width: 200px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    .job h3 { color: #0066ff; margin: 5px 0; font-size: 16px; }
  </style>
</head>
<body>
  <header>
    <h3>Varun Tech</h3>
    <nav>
      <a href="#">Home</a><a href="#">Browse Job</a><a href="#">Pages</a>
      <a href="#">Blog</a><a href="#">Contact</a>
    </nav>
    <div>
      <a href="#" class="btn btn-orange">Log In</a>
      <a href="#" class="btn btn-green">Post a Job</a>
    </div>
  </header>

  <section class="hero">
    <p>4536+ Jobs listed</p>
    <h2>Find Your Dream Job</h2>
    <p>Explore jobs at Varun Tech and other top companies.</p>
    <a href="#" class="btn btn-green">Upload Resume</a>
  </section>

  <div class="search">
    <input type="text" placeholder="Keyword">
    <input type="text" placeholder="Location">
    <select><option>Category</option><option>IT</option><option>Finance</option></select>
    <button>Find Job</button>
  </div>

  <section class="jobs">
    <div class="job"><h3>Web Developer</h3><p>Noida</p><a href="#" class="btn btn-green">Apply</a></div>
    <div class="job"><h3>Python Developer</h3><p>Delhi</p><a href="#" class="btn btn-green">Apply</a></div>
    <div class="job"><h3>UI/UX Designer</h3><p>Remote</p><a href="#" class="btn btn-green">Apply</a></div>
  </section>

  <footer>&copy; 2025 Varun Tech - Job Board</footer>
</body>
</html>
