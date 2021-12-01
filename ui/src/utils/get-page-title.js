import defaultSettings from '@/settings'

const title = defaultSettings.title || 'Resource Management Dashboard'

export default function getPageTitle(pageTitle) {
  if (pageTitle) {
    return `${pageTitle} - ${title}`
  }
  return `${title}`
}
