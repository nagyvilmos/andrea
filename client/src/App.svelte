<!-- App.svelte -->
<script>
  import { Router, Route } from "svelte-routing";
  import Layout from "./lib/Layout.svelte";
  import Home from "./routes/Home.svelte";
  import About from "./routes/About.svelte";
  import ArticleList from "./routes/ArticleList.svelte";
  import Article from "./routes/Article.svelte";
  import Contact from "./routes/Contact.svelte";
  import Companies from "./routes/Companies.svelte";
  import Programme from "./routes/Programme.svelte";

  const currentPath=window.location.pathname;

</script>

<Router
  url={currentPath} 
>
  <Layout {currentPath} wide={currentPath==="/companies"}>
  <div>
    <Route path="/article/:id" let:params>
      <Article id="{params.id}" />
    </Route>
    <Route path="/article" component={ArticleList} />
    <Route path="/about" component={About} />
    <Route path ="/contact" component={Contact} />
    <Route path ="/companies" component={Companies} />
    <Route path ="/programme" component={Programme} />
    <Route path="/" component={Home} />
  </div>
</Layout>
</Router>
