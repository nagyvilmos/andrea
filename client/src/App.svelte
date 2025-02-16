<!-- App.svelte -->
<script>
  import { fade } from "svelte/transition";
  import { Router, Link, Route } from "svelte-routing";
  import Home from "./routes/Home.svelte";
  import About from "./routes/About.svelte";
  import Blog from "./routes/Blog.svelte";
  import BlogPost from "./routes/BlogPost.svelte";
  import Layout from "./lib/Layout.svelte";
  import Contact from "./routes/Contact.svelte";
    import Companies from "./routes/Companies.svelte";

  export let url = "";
</script>

<Router
  {url} viewtransition={() => ({ fn: fade, duration: 321 })}
>
  <Layout url>
  <div>
    <Route path="/blog/:id">
      <BlogPost id />
    </Route>
    <Route path="/blog" component={Blog} />
    <Route path="/about" component={About} />
    <Route path ="/contact" component={Contact} />
    <Route path ="/companies" component={Companies} />
    <Route path="/" component={Home} />
  </div>
</Layout>
</Router>
