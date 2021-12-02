import Cookies from 'js-cookie'

const TokenKey = 'Admin-Token'

export function getToken() {
  return Cookies.get(TokenKey)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

export function setUserCookie(user_name){
  return Cookies.set("login.form.username",user_name)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}
