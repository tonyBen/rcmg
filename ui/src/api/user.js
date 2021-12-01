import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/api/authz/user/login',
    params:data,
    method: 'post'
  })
}

export function getInfo(token) {
  return request({
    url: '/api/authz/user/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/api/authz/user/logout',
    method: 'post'
  })
}
