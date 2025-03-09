// @ts-nocheck

// down at the bottom will be this:
export async function getData(url, method = "GET", data = undefined, options = {}) {

  const callOptions = { ...options, method };
  if (data !== undefined) {
    callOptions.headers = {
      "Content-Type": "application/json",
    };
    callOptions.data = JSON.stringify(data);

  }

  const res = await fetch(`/api/${url}`, callOptions);

  if (!res.ok) {
    throw new Error(res.statusText);
  }
  const ret = await res.json();
  return ret;
}
