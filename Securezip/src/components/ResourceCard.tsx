import { ExternalLink, Wrench, Video, FileText, Tag } from 'lucide-react';
import { Resource } from '../types';

interface ResourceCardProps {
  resource: Resource;
}

export function ResourceCard({ resource }: ResourceCardProps) {
  const getIcon = () => {
    switch (resource.type) {
      case 'tool':
        return <Wrench className="w-5 h-5" />;
      case 'video':
        return <Video className="w-5 h-5" />;
      case 'paper':
        return <FileText className="w-5 h-5" />;
    }
  };

  const getTypeColor = () => {
    switch (resource.type) {
      case 'tool':
        return 'bg-blue-100 text-blue-700 border-blue-200';
      case 'video':
        return 'bg-red-100 text-red-700 border-red-200';
      case 'paper':
        return 'bg-green-100 text-green-700 border-green-200';
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200 hover:shadow-md transition-all duration-200 hover:-translate-y-0.5">
      <div className="p-6">
        <div className="flex items-start justify-between mb-3">
          <div className="flex items-center gap-2">
            <div className={`p-2 rounded-lg border ${getTypeColor()}`}>
              {getIcon()}
            </div>
            <div>
              <h3 className="font-semibold text-lg text-gray-900 leading-tight">
                {resource.title}
              </h3>
              {resource.author && (
                <p className="text-sm text-gray-500 mt-0.5">{resource.author}</p>
              )}
            </div>
          </div>
          {resource.featured && (
            <span className="px-2.5 py-1 bg-yellow-100 text-yellow-800 text-xs font-medium rounded-full border border-yellow-200">
              Featured
            </span>
          )}
        </div>

        <p className="text-gray-600 text-sm leading-relaxed mb-4">
          {resource.description}
        </p>

        <div className="flex flex-wrap gap-2 mb-4">
          {resource.tags.slice(0, 4).map((tag) => (
            <span
              key={tag}
              className="inline-flex items-center gap-1 px-2.5 py-1 bg-gray-100 text-gray-700 text-xs rounded-md"
            >
              <Tag className="w-3 h-3" />
              {tag}
            </span>
          ))}
        </div>

        <div className="flex items-center justify-between pt-4 border-t border-gray-100">
          <span className="text-xs text-gray-500 capitalize">{resource.category}</span>
          <a
            href={resource.url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 px-4 py-2 bg-gray-900 text-white text-sm font-medium rounded-lg hover:bg-gray-800 transition-colors"
          >
            View Resource
            <ExternalLink className="w-4 h-4" />
          </a>
        </div>
      </div>
    </div>
  );
}
