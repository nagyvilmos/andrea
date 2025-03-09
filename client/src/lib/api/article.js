import {getData} from "./index";

export const getArticleList = async () => await getData('article');
export const getArticle = async (id) => await getData(`article/${id}`);
